#!/usr/bin/env python
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image


def callback(ros_data):



    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(ros_data, desired_encoding="passthrough")
    cv2.imshow('video',cv_image)
    cv2.waitKey(1)



def listener():
    rospy.init_node('CompressedImage', anonymous = True)
    rospy.Subscriber("/camera/rgb/image_raw",Image,callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
