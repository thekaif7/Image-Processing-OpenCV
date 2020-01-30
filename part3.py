import numpy as np
import cv2

img = cv2.imread('naruto.jpg', cv2.IMREAD_COLOR)
#parameter of line --> image,start point,end point ,color in BGR , pixel;
cv2.line(img , (0,0),(150,150),(255,255,255), 15)
cv2.rectangle(img,(10,10),(200,150),(0,250,0),5)
#parameter of circle --> image,centre point , radius ,color BGR , pixel (-1 fill the circle)
cv2.circle(img,(100,100),55,(0,0,255),-1)

#polylines -> images, points atleast 2, True , BGR , Pixel(-1 not fill )
pts = np.array([[10,5],[20,30],[70,100],[50,10]],np.int32)
# print(pts.shape)
# pts = pts.reshape((-1,2,4))
# print(pts.shape)
# print(pts)
cv2.polylines(img,[pts],True,(0,5,150),3)

#text -> image,title,strat point, font ,size,color,thickness , cv2.LINE_AA
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"Naruto",(50,100),font,1,(0,0,0),1,cv2.LINE_AA)



cv2.imshow('image_',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
