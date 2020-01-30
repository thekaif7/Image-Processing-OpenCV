import cv2
import numpy as np
import json
import math

img = cv2.imread("blue.png")
imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
lower = np.array([20,50,220])       #[200,75,70])
upper = np.array([100,100,255])    # [255,100,120])
mask = cv2.inRange(imghsv, lower, upper)
# _,contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) for opencv 3.3
contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cord = []
im = np.copy(img)
for cnt in contours:


    # cv2.drawContours(im, cnt, -1, (0, 0, 0), 2)
    x,y,w,h = cv2.boundingRect(cnt)
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    # M = cv2.moments(cnt)
    M = cv2.moments(cnt)
    x = int((M['m10']) / (M['m00']+0.000001))
    y = int((M['m01']) / (M['m00']+0.000001))
    if x!=0.0 or y!=0.0:
        cord.append([x,y])
    # print(x ,y)
    # cv2.Rectangle(im,(int(x),int(y)),5,(0,0,0),-1)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(im,"count",(x,y),font,1,(0,255,0),1,cv2.LINE_AA)
# print(cord)
with open('3_3_v2_cord.json') as f:

    data = json.load(f)
print(len(cord))
for i in cord:
    min_dis = 100000000000
    loc = ""
    for location , xy in data.items():
        font = cv2.FONT_HERSHEY_SIMPLEX

        cv2.putText(im,loc,(xy[0],xy[1]),font,0.5,(255,255,100),1,cv2.LINE_AA)

        dis = math.sqrt(abs(xy[0]-i[0])**2+abs(xy[1]-i[1])**2)
        # print(min_dis,dis)
        if dis < min_dis:
            loc = location
            min_dis = dis
            # print(loc)


    font = cv2.FONT_HERSHEY_SIMPLEX
    # print(loc)
    cv2.putText(im,loc,(i[0],i[1]),font,1,(0,255,0),1,cv2.LINE_AA)

cv2.imshow("frame",im)
cv2.imshow("mask",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
