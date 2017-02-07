#!/usr/bin/env python
import rospy
import wiringpi
import subprocess
import time
from std_msgs.msg import Int32

n = 0
temp = 23

def cb(count):
    global n,temp
    n = count.data
    if n:
        io.digitalWrite(23, 0)
        io.digitalWrite(24, 0)
        io.digitalWrite(25, 0)
        io.digitalWrite(26, 0)
        if temp > 26:
            temp = 23
        io.digitalWrite(temp, 1)
        temp += 1
    rospy.loginfo(n)


if __name__ == '__main__': 
    subprocess.check_call('gpio export 23 out', shell = True)
    subprocess.check_call('gpio export 24 out', shell = True)
    subprocess.check_call('gpio export 25 out', shell = True)
    subprocess.check_call('gpio export 26 out', shell = True)
    io = wiringpi.GPIO(wiringpi.GPIO.WPI_MODE_GPIO_SYS)
    io.pinMode(23,io.OUTPUT)
    io.pinMode(24,io.OUTPUT)
    io.pinMode(25,io.OUTPUT)
    io.pinMode(26,io.OUTPUT)

    rospy.init_node('led')
    sub = rospy.Subscriber('time_count', Int32, cb)

    rospy.spin()

