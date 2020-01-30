import numpy as np
import cv2

img = cv2.imread('naruto.jpg',cv2.IMREAD_COLOR)

#extract image pixel information(mainly BGR value)
px = img[55,55]
print(px)

#modify Pixel
img[55,55] = [20,20,20]
px = img[55,55]
print(px)
#region of image -> pixel vary of a subimage in image eg: nose , face ,eyes 
#roi parameter [x1->x2 , y1->y2 ]
# img[50:150,50:150] = [250,0,250]

#duplicate
roi = img[50:150,50:150]
img[0:100,0:100] = roi #should have same variation

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
