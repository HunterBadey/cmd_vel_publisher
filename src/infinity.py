#! /usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist

rospy.init_node('infinity_publisher')
pub = rospy.Publisher ('/cmd_vel', Twist)

rate = rospy.Rate(100)
velocity = Twist()
velocity.linear.x = 1
velocity.angular.z = (math.pi / 4)
time = 0

while not rospy.is_shutdown(): 
  pub.publish(velocity)
  time = time + 0.01
  rate.sleep()
  if time >= (8):
    velocity.angular.z = velocity.angular.z * (-1)
    time = 0
  