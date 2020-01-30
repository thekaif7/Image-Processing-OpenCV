import numpy as np
import cv2

img1 = cv2.imread("naruto.jpg")
img2 = cv2.imread("bg.png")

# # add_superImpose = img1+img2 #superimposed two image into one without reduce opaque
# # add_bgr = cv2.add(img1,img2) # add both bgr into one bgr value
#
# weighted = cv2.addWeighted(img1,0.4,img2,0.6,0)
#
#
#
# cv2.imshow("weighted",weighted)
# # cv2.imshow("bgr adding",add_bgr)
logo = cv2.imread("naruto.jpg")
#masking
rows,cols,channel = logo.shape
roi = img2[250:250+rows,300:300+cols]
img2gray = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)
#threshold --> image , threshold value ,set value , method(binary_inv black or white)
#if any pixel any rgb value is less than threshold then it set to 0 otherwise set to set value
#basically it use in remove white foreground color
ret , mask = cv2.threshold(img2gray,210,255,cv2.THRESH_BINARY_INV)

#extract only black area(unmask area) of mask
mask_inv = cv2.bitwise_not(mask)

#now using mask_inv we set bg of logo of img2 pexel.
imgBG = cv2.bitwise_and(roi,roi,mask=mask_inv)
#same for foreground ,mask here is the area where pexel will assign
imgFG = cv2.bitwise_and(logo,logo,mask=mask)

#adding bgr value of two image into one image
dist = cv2.add(imgFG,imgBG)
#update the image pexel
img2[250:250+rows,300:300+cols] = dist





# cv2.imshow('mask',mask)
# cv2.imshow('mask_inv',mask_inv)
cv2.imshow("final image",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
