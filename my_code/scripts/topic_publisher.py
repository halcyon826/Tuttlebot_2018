#!/usr/bin/env python
import rospy

from std_msgs.msg import Int32

def talker():
    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('chatter', Int32, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    count = 0
    while not rospy.is_shutdown():
        rospy.loginfo(count)
        pub.publish(count)
        count +=1
        rate.sleep()
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
