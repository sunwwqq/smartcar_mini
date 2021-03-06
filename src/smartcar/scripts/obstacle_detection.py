#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import rospy
from std_msgs.msg import Bool
from sensor_msgs.msg import LaserScan

class rplidarDetector:
    def __init__(self):
        self.min_dist = 0
        self.has_obs = Bool()

        rospy.init_node('obstacle_detection', anonymous=True)
        rospy.Subscriber('/scan', LaserScan, self.callback)
        self.pub = rospy.Publisher('has_obs', Bool, queue_size=1)
        print 'LiDAR is OK'

    def callback(self, msg):
        minIndex = 1

        # goes throgh  array and find minimum  on the right 
        '''
        for i in range (1, 11):
            if msg.ranges[i] < msg.ranges[minIndex] and msg.ranges[i] > 0.05:
                minIndex = i
        for i in range (340, 350):
            if msg.ranges[i] < msg.ranges[minIndex] and msg.ranges[i] > 0.05:
                minIndex = i
        '''
        for i in range (600, 840):
            if msg.ranges[i] < msg.ranges[minIndex] and msg.ranges[i] > 0.05:
                minIndex = i

        # calculate distance
        self.min_dist = msg.ranges[minIndex]

        #public message
        if self.min_dist < 1.0:
            print "min_dist = "+ str(self.min_dist) + ", stop"
            self.has_obs.data = True
            self.pub.publish(self.has_obs)
        else:
            self.has_obs.data = False
            self.pub.publish(self.has_obs)

if __name__ == '__main__':
    try:
        detector = rplidarDetector()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
