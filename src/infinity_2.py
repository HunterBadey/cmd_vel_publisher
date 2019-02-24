#! /usr/bin/env python

import rospy
import math
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

rospy.init_node('infinity_publisher2')
pub = rospy.Publisher ('/cmd_vel', Twist)


orientation = Odometry()
orientation.position.xold = 0
orientation.position.xnew = 0
orientation.position.xtotal = 0

def distance_calculator:
  orientation.position.xnew = orientation.position.xold + (1* .01)
  orientation.position.xtotal = (orientation.position.xnew - orientation.position.xold) + orientation.position.xtotal
  orientation.position.xold = orientation.position.xnew

rate = rospy.Rate(100)
velocity = Twist()
velocity.linear.x = 1
velocity.angular.z = 0.5

while not rospy.is_shutdown(): 
  pub.publish(velocity)
  sub = rospy.Subscriber ('/odom', Odometry, distance_calculator)
  rate.sleep()
  if orientation.position.xtotal >= (4 * math.pi):
    velocity.angular.z = velocity.angular.z * (-1)
    
  