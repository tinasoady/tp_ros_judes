#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
from std_msgs.msg import Bool
import numpy as np
import math
Button = [False]

def talker(Button):
	pub = rospy.Publisher('chatter', PoseStamped, queue_size=10)
	rospy.init_node('talker', anonymous=True)
	rate = rospy.Rate(15) # 15hz
	msg = PoseStamped()
	print(msg)
	msg.header.frame_id="map"
	t = - math.pi
	while not rospy.is_shutdown():
		#rayon = 0.5
		while t <=  math.pi :	
			listener(Button)
			if not Button[0]:
				continue
				   
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(msg.pose.position.x)
			t = t + 0.1
			#hello_str = "hello world %s" % rospy.get_time()
			#rospy.loginfo(hello_str)
			pub.publish(msg)
			rate.sleep()
			
		while t >=  -math.pi :	
			listener(Button)
			if not Button[0]:
				continue   
				 
			msg.pose.position.x = t
			msg.pose.position.y = np.sin(- msg.pose.position.x)
			t = t - 0.1
			#hello_str = "hello world %s" % rospy.get_time()
			#rospy.loginfo(hello_str)
			pub.publish(msg)
			rate.sleep()

		

def callback(button,data):
    button[0] = data.data
    

def listener(Button):
	rospy.Subscriber('button_state', Bool, lambda data,button=Button:callback(button,data))

if __name__ == '__main__':
    try:
    	talker(Button)
    except rospy.ROSInterruptException:
    	ass
