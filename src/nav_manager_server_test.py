#!/usr/bin/env python


#REPLACE CODE WITH YOUR ROS2 NAV MANAGER + ROS BRIDGE

from __future__ import print_function

from suii_communication_ros1.srv import TableGoal
import rospy

def start_navigation(req):
    #HERE YOU WILL INTEGRATE YOUR NAVIGATION SOFTWARE
    print("Goal acchieved")
    return True

def nav_manager_server_test():
    rospy.init_node('nav_manager_server_test')
    s = rospy.Service('table_goal', TableGoal, start_navigation)
    print("Ready to navigate")
    rospy.spin()

if __name__ == "__main__":
    nav_manager_server_test()