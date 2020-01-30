import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()

	# create NumPy arrays from the boundaries

    img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([100, 100, 84], dtype = "uint8")

    upper = np.array([179, 255, 255], dtype = "uint8")

	# find the colors within the specified boundaries and apply
	# the mask
    mask = cv2.inRange(img, lower, upper)

    output = cv2.bitwise_and(frame, frame, mask = mask)
    median = cv2.medianBlur(output,15)

	# show the images
    cv2.imshow("images", np.hstack([frame, median]))
    cv2.imshow("median", median)
	# cv2.waitKey(0)
    # # Convert BGR to HSV
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #
    #
    # # img = cv2.imread("bluepink.jpg")
    # # imghsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])
    # mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    # contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # im = np.copy(frame)
    # cv2.drawContours(frame, contours, -1, (0, 255, 0), 1)
    #
    # # define range of blue color in HSV
    # lower_blue = np.array([110,50,50])
    # upper_blue = np.array([130,255,255])
    # # Threshold the HSV image to get only blue colors
    # mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # # Bitwise-AND mask and original image
    # res = cv2.bitwise_and(frame,frame, mask= mask)
    # cv2.imshow('frame',frame)
    # # cv.imshow('mask',mask)
    # # cv.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
