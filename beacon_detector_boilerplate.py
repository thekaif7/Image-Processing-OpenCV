#!/usr/bin/env python
from __future__ import print_function
import roslib
import sys
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import Image
from survey_and_rescue.msg import *
from cv_bridge import CvBridge, CvBridgeError
import random
import pickle
import imutils
import copy
import json

class sr_determine_colors():

	def __init__(self):
		self.detect_info_msg = SRInfo()
		self.bridge = CvBridge()
		self.detect_pub = rospy.Publisher("/detection_info",SRInfo,queue_size=10)
 		self.image_sub = rospy.Subscriber("/usb_cam/image_rect_color",Image,self.image_callback)
 		self.serviced_sub = rospy.Subscriber('/serviced_info',SRInfo,self.serviced_callback)

		# list of all detect coordinate
		self.cord = []



	def load_rois(self, file_path = 'rect_info.pkl'):
		try:
			# s.rois = np.load("rois.npy")
			with open(file_path, 'rb') as input:
   				self.rect_list = pickle.load(input)
		except IOError, ValueError:
			print("File doesn't exist or is corrupted")


 	def image_callback(self, data):
 		try:
 			self.img = self.bridge.imgmsg_to_cv2(data, "bgr8")
 		except CvBridgeError as e:
 			print(e)


 	def serviced_callback(self, msg):
 		pass

	def detect_color_contour_centers(self, color_str):
		colors = {"Blue":[110,50,50],[130,255,255]; "Red":[0,120,100],[5,175,210] ; "Green":[20,42,90],[180,255,180]}
		# img = cv2.imread("shape.png")
		for color,cord in colors:

			imghsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
			lower_blue = np.array(colors[0])
			upper_blue = np.array(colors[1])
			mask_blue = cv2.inRange(imghsv, lower_blue, upper_blue)
		# _,contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) for opencv 3.3
			contours, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			for cnt in contours:
				im = np.copy(self.img)
				# cv2.drawContours(im, cnt, -1, (0, 0, 0), 2)
				M = cv2.moments(cnt)
			# M = cv2.moments(cnt)
				# x = int(M['m10'] / M['m00'])
				# y = int(M['m01'] / M['m00'])
				x,y,w,h = cv2.boundingRect(cnt)
				if x!=0 or y!=0:

					self.cord.append([x,y,color])
			# font = cv2.FONT_HERSHEY_SIMPLEX
			# cv2.putText(im,str(x)+","+str(y),(x,y),font,0.5,(0,0,0),1,cv2.LINE_AA)
		cv2.imshow("frame",im)
		cv2.waitKey(0)
		cv2.destroyAllWindows()



	def check_whether_lit(self):
		with open('cord.json') as f:

  			data = json.load(f)
		min_dis = 1000000
		info = {}
		for color_xy in self.cord:
			x = color_xy[0]
			y = color_xy[1]
			color = color_xy[2]

			for loc , xy in data:
				dis = math.sqrt(abs(xy[0]-x)**2 + abs(xy[1]-y)**2)
				if dis<min_dis:
					min_dis = dis
					location = loc
			info[color] = location,




def main(args):

	try:
		rospy.init_node('sr_beacon_detector', anonymous=False)
		s = sr_determine_colors()
		'''You may choose a suitable rate to run the node at.
		Essentially, you will be proceesing that many number of frames per second.
		Since in our case, the max fps is 30, increasing the Rate beyond that
		will just lead to instances where the same frame is processed multiple times.'''
		rate = rospy.Rate(30)
		# rate = rospy.Rate(5)
		s.load_rois()
		while s.img is None:
			pass
	except KeyboardInterrupt:
		cv2.destroyAllWindows()
	while not rospy.is_shutdown():
		try:
			s.detect_color_contour_centers()
			s.check_whether_lit()
			rate.sleep()
		except KeyboardInterrupt:
			cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
