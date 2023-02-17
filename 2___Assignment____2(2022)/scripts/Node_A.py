#! /usr/bin/env python3 


# import the necessary libraries
import rospy
from geometry_msgs.msg import PoseStamped 
import actionlib.msg 
import assignment_2_2022.msg 
import actionlib
import rospy
from nav_msgs.msg import Odometry
from rt1_2nd_assignment.msg import odom_custom_msg
import os

#global variable
start=1




#target_client function

def target_client():

    x_position = input("\nX position: ")
    y_position = input("Y position: ")

 
    x_position = int(x_position)
    y_position = int(y_position)
 
    print("\nWating for connection")

    #Wait for the server to be ready to receive goals 
    client.wait_for_server()

    #Creates a goal to send to the action server.
    goal = PoseStamped()


    goal.pose.position.x = x_position
    goal.pose.position.y = y_position


    goal = assignment_2_2022.msg.PlanningGoal(goal)

    
    #Sends the goal to the action server.
    client.send_goal(goal)
    print("\nGoal sent")
    input("\n\nEnter to select again")

    #Back to the interface function 
    interface()
      

#cancel_target function 
def cancel_target():

    #Cancel the goal that is sent to the action server
    client.cancel_goal()
    print(f"\ncanceled")
    input("\n\nEnter to select again")
    #Back to the interface function
    interface()


#wrong function

def wrong():
    print("Wrong input")
    rospy.sleep(2)
    interface()


#interface function

def interface():

    os.system('clear')
    print("1:Input Targert\n")
    print("2:Cancel\n")
    print("3:Close\n")   

    #Ask the user to select an operation
    user_selection = input("Select: ")
    
    #Check the user selection
    if   (user_selection == "1"):
        target_client()

    elif (user_selection == "2"):
        cancel_target() 

    elif (user_selection == "3"):
        exit()

    else:
        wrong()

#start_description function
def start_description(start_description_flag):
    if start_description_flag == 1:
        os.system('clear')
        print("\nNode A\n")
        input("Enter to see menu")

        start_description_flag=0   


#callback function

def callback(data):
    
    my_publisher = rospy.Publisher('position_and_velocity', odom_custom_msg, queue_size=5)
    my_custom_message = odom_custom_msg()
    my_custom_message.x = data.pose.pose.position.x
    my_custom_message.y = data.pose.pose.position.y
    my_custom_message.vel_x = data.twist.twist.linear.x
    my_custom_message.vel_y = data.twist.twist.linear.y

    my_publisher.publish(my_custom_message)



if __name__ == '__main__':
    #This is the starting point of the program, so all of the code below this line will be executed.

    start_description(start)
    #This function is used to set the initial starting point and any other variables needed for the program to begin.

    rospy.init_node('NodeA')
    #This functions initializes a ROS node with the name "NodeA". This allows other nodes to communicate and interact with this node.

    rospy.Subscriber("/odom", Odometry, callback)
    #This subscribes to the "/odom" topic, and any messages received on this topic will be sent to the "callback" function. This allows us to accept incoming data from the Sensor Fusion node.

    client = actionlib.SimpleActionClient('/reaching_goal',assignment_2_2022.msg.PlanningAction )
    #This creates a simple action client called "client". It is used to call the service "/reaching_goal" and use messages from the assignment_2_2022 message type "PlanningAction".

    interface()
    #This function is used to get input from a user (i.e keyboard) and then process that input.

    rospy.spin()
    #This line is used to keep the program running; if it is omitted, the program will terminate immediately.

