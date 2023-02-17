#!/usr/bin/env python3

# import the necessary libraries
import math
from rt1_2nd_assignment.msg import odom_custom_msg
import rospy
import os

#global variables
start_description_flag=1
counter =0
temp_vel =0
avg_vel =0
des_pos_distance=0
sequence = 1




#callback function
def callback_subscriber(data):

    #global variables
    global counter
    global temp_vel
    global avg_vel
    global des_pos_distance

    #get the desired position from the parameter server
    des_pos_x = rospy.get_param("/des_pos_x")
    des_pos_y = rospy.get_param("/des_pos_y")

    #get the current position of the robot
    cur_pos_x = data.x
    cur_pos_y = data.y

    #calculate the distance of the robot from the target
    des_pos_distance= math.sqrt(((des_pos_x - cur_pos_x)**2)+((des_pos_y - cur_pos_y)**2))


    #current velocity is stored in the cur_vel variable
    cur_vel_x = data.vel_x
    cur_vel_y = data.vel_y

    #calculate the current velocity of the robot
    cur_vel= math.sqrt(((cur_vel_x)**2)+((cur_vel_y)**2))


    #calculate the average velocity of the robot
    if counter<5:

        temp_vel=temp_vel+cur_vel
        counter +=1

    elif counter==5:

        counter=0
        temp_vel /= 5
        avg_vel=temp_vel
        temp_vel=0


#start_description function
def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\nNode C\n")
        input("\nEnter to continue!")
        start_description_flag=0   


    


#main function
if __name__ == "__main__":

    # call the start_description() function with start_description_flag as argument
    start_description(start_description_flag)
    # Log level warning to notify that the service is started
    rospy.logwarn("service started")
    # initiating a node
    rospy.init_node('NodeC')
    # get the value of parameter '/print_interval'
    HZ=rospy.get_param("/print_interval")
    # set the rate accordingly
    rate = rospy.Rate(HZ)
    # Subscribing to the position and velocity topic
    rospy.Subscriber("position_and_velocity", odom_custom_msg, callback_subscriber)
    # loop till shutdown
    while not rospy.is_shutdown():
        # Print sequence, distance to target and robot's average velocity
        print(f"Sequence: {sequence}")
        print(f"distance to target: {des_pos_distance : .3f}")
        print(f'Robot’s average velocity: {avg_vel: .3f}')
        print(f"---------------------------")
        # Increase the sequence number
        sequence += 1
        # Sleep for one cycle
        rate.sleep()
