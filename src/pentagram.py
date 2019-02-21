#! /usr/bin/env python
import rospy
import math
from geometry_msgs.msg import Twist 

rospy.init_node('pentagram_publisher')
pub = rospy.Publisher ('/cmd_vel', Twist)

rate = rospy.Rate(1)
velocity = Twist()

velocity.linear.x = 1
velocity.angular.z = 0

time = 0

while not rospy.is_shutdown(): 
  pub.publish(velocity)
  time = time + 1
  rate.sleep()
  if time == 1 and velocity.angular.z== 0:
    time = 0 
    velocity.linear.x = 0
    velocity.angular.z = (.8 * math.pi) / 2
  if time == 2 and velocity.linear.x == 0:
    time = 0
    velocity.angular.z = 0
    velocity.linear.x = 1
  