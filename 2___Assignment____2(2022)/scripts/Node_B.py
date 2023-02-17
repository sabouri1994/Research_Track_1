#!/usr/bin/env python3


# import the necessary libraries
import rospy
from std_srvs.srv import Empty,EmptyResponse
import assignment_2_2022.msg
import os



#global variables
reached_goal_counter = 0
canceled_goal_counetr = 0
sequence = 1 
start_description_flag = 1
print_flag = True

#callback function
def callback_service(req):
    global canceled_goal_counetr , reached_goal_counter , sequence
    print("-------------------------------------")
    print(f"Sequence: {sequence}\nNumber of canceled goal: {canceled_goal_counetr}\nnumber of reached goal: {reached_goal_counter}")
    print("-------------------------------------")
    sequence += 1
    return EmptyResponse()


#callback function
def callback_subscriber(data):

    if data.status.status == 2:

        global canceled_goal_counetr
        canceled_goal_counetr += 1
    
    elif data.status.status == 3:

        global reached_goal_counter
        reached_goal_counter += 1

#start_description function
def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\nNode B\n")
        input("\nEnter to continue!")
        start_description_flag=0   



#main function
if __name__ == "__main__":
#This evaluates to True if the source file being execute is the main program. This is useful in multi-file programs, as it allows you to control which file is executing and when.

    start_description(start_description_flag)
    #This function is used to set a flag that is used to indicate whether the program should describe itself or not.

    rospy.logwarn("service started")
    #This logs a warning stating that the service has been started.

    rospy.init_node('NodeB')
    #This code initializes the node called NodeB with the rospy package, which provides the communication functions for communicating with other nodes in the ROS system.

    rospy.Subscriber("/reaching_goal/result", assignment_2_2022.msg.PlanningActionResult, callback_subscriber)
    #This code subscribes to the topic /reaching_goal/result, which is of type assignment_2_2022.msg.PlanningActionResult, and calls the callback_subscriber function when a message is received.

    rospy.Service('reach_cancel_ints', Empty, callback_service)
    #This code registers the service reach_cancel_ints, which is of type Empty, and calls the callback_service function when the service is called.

    rate = rospy.Rate(1)
    #This sets the rate of the loop to 1 Hz, meaning that this loop will run once every second.

    while not rospy.is_shutdown():
        #This code creates an infinite loop and will keep running until rospy.is_shutdown() returns True.

        if print_flag== True:
        #This code checks the print_flag to see if it is True or False. If it is True it prints a message.

            print("waiting for a client to call the service ...")
            #This prints out a message to the user letting them know the program is waiting for someone to call the service.

            print_flag = not print_flag
    #This code toggles the value of the print_flag, meaning that if it was True, it will now be False and vice versa.

        rate.sleep()
    #This code pauses the loop for the amount of time set by the rate set earlier, in this case 1 second. This helps prevent CPU usage from reaching high levels.