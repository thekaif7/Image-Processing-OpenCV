import numpy as np
import cv2

img = cv2.imread("flex_sheet_task3_3.png")
# img = cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow("blur",img)




gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(gray,-1,kernel)
edged = cv2.Canny(gray, 180, 240)


# _ , threshold = cv2.threshold(img,240,255,cv2.THRESH_BINARY)


contours, hierarchy = cv2.findContours(edged,
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

# contour, _ = cv2.findContours(threshold,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# print(contour.shape)
count=1
cord = []
for cnt in contours:
    approx = cv2.approxPolyDP(cnt, 0.01*cv2.arcLength(cnt, True), True)
    if 3<len(approx)<=5:

        # cv2.drawContours(img, [approx], 0, (0,255,0), 2)
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # x = approx.ravel()[0]
        # y = approx.ravel()[1]
        #
        # # k = cv2.isContourConvex(cnt)
        # # print(count,k)
        x,y,w,h = cv2.boundingRect(cnt)
        # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        # M = cv2.moments(cnt)
        # cX = int(M['m10'] / M['m00'])
        # cY = int(M['m01'] / M['m00'])
        if 1000<w*h<=10000:
            font = cv2.FONT_HERSHEY_SIMPLEX
            x = approx.ravel()[0]
            y = approx.ravel()[1]


            # k = cv2.isContourConvex(cnt)
            # print(count,k)
            # x,y,w,h = cv2.boundingRect(cnt)
            # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            M = cv2.moments(cnt)
            cX = int(M['m10'] / M['m00'])
            cY = int(M['m01'] / M['m00'])
            cord.append([cX,cY])
            # cv2.putText(img,str(count),(cX,cY),font,0.5,(0,0,255),2,cv2.LINE_AA)
            # print(w*h , count)
            # count+=1
    # x = approx.ravel()[0]
    # y = approx.ravel()[1]

    # if len(approx)==4:
#     cord.append([x,y])
# cord = sorted(cord)
# for xy in cord:
#     x = xy[0]
#     y = xy[1]

        # font = cv2.FONT_HERSHEY_SIMPLEX
        # cv2.putText(img,str(count),(x,y),font,1,(0,0,0),1,cv2.LINE_AA)
        # count+=1
    # print(x,y)
cord = sorted(cord,reverse = True , key = lambda x: x[1] )


count = 0
for i in range(0,35):
    x = cord[i][0]
    y = cord[i][1]

    rem = (i)%6
    if rem ==0:
        count+=1
    # rem = 6 -rem
    char= chr(ord("A")+rem)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img,str(char+str(count)),(x,y),font,0.5,(0,255,0),1,cv2.LINE_AA)
    print("coordinate {0} {1} count : {2} {3} ".format(x,y,str(char),ord(char)))







#
# for i in cord:
#     x = i[0]
#     y = i[1]
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     cv2.putText(img,str(count),(x,y),font,0.5,(0,255,0),1,cv2.LINE_AA)
#     print("coordinate {0} {1} count : {2} ".format(x,y,count))
#     count+=1


cv2.imshow("img",img)
cv2.imshow("edge",edged)
cv2.waitKey(0)
cv2.destroyAllWindows()
