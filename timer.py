#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

if __name__ == '__main__': 
    rospy.init_node('timer')
    pub = rospy.Publisher('time_count', Int32, queue_size=1)
    rate = rospy.Rate(1)
    n = 1
    while not rospy.is_shutdown():
        pub.publish(n)
        rate.sleep()
