# Research Track 1
# Genova University 
Professor: [Carmine Recchiuto](https://github.com/CarmineD8 "Carmine Recchiuto")\
Student: [Mohammad Sabouri]
Assignment___2\
Submitted Date: 2023-17-02
S5659227


# Robotic 3D Simulation with Gazebo and ROS
This project is a robotic simulation that utilizes the main core features of ROS to create software for robots. This implementation includes a command-line based user interface to send positional goals to the robot, nodes communication based on costom messages and publisher-subscriber architecture, as well as ROS services and action servers to implement tasks like goal summaries, robot planning, and navigation. Lastly, launch files are used to set global parameters and manage the running of multiple nodes.

# Command-line User Interface:
Sending positional goals to the robot through a command-line based user interface for easy and efficient communication.

-**Custom Message Publisher-Subscriber:** Nodes communicate using custom messages and publisher-subscriber architecture, this allows nodes to easily send and receive messages in real time.

-**ROS Services:** ROS services are used to perform short-running tasks like reporting the goal summary.

-**ROS Actions Servers:** The long-running tasks such as robot planning and navigation are handled by ROS action servers.

-**Launch Files:** Launch files are utilized to set global parameters and manage multiple running nodes.
When downloaded, this robotic simulation would include a complete README file documenting the use of the main core features and an example of the code in action.

# Main Core Features of this Implementation
This robotic simulation utilizes the main core features of ROS to create robot softwares. The features allow for command-line-based user interfaces to send positional goals to robots and nodes communication based on custom messages and publisher-subscriber architecture. Additionally, short and long running tasks, such as reporting a goal summary or robot navigation, are handled using ROS services and action servers. Furthermore, launch files are used to set global parameters and manage running of multiple nodes.

-**Running the Simulation**
The program can be run by entering the command:
```bash
$ roslaunch rt1_project_2 project_2.launch
```
-**Command-line User Interface**
The command-line user interface allows for easy and efficient communication between the user and the robot. The user can send positional goals to the robot by entering the command:
```bash
$ rostopic pub -1 /goal geometry_msgs/Pose2D "x: 0.0 y: 0.0 theta: 0.0"
```
-**Custom Message Publisher-Subscriber**
Nodes communicate using custom messages and publisher-subscriber architecture, which allows nodes to easily send and receive messages in real time. The custom message is defined in the file msg/Goal.msg. The publisher node is defined in the file src/goal_publisher.py. The subscriber node is defined in the file src/goal_subscriber.py.

-**ROS Services**
Services are an important component of the ROS architecture, allowing nodes to communicate and carry out tasks together. Services allow nodes to exchange data and messages in a coordinated and efficient way. For example, one node may advertise a service to turn on an LED, and another node can call that service when needed. This type of communication is essential for robotic systems that need to interact with real-world environments and take actions based on sensor data. Additionally, services can be utilized to perform short-running tasks like reporting the goal summary or long-running tasks such as robot planning and navigation.

Services can also be used to initiate tasks such as sending positional goals to the robot, gathering data from wheel encoders, and even more complex tasks such as controlling the behavior of multiple robots. This flexibility makes services one of the most useful components of the ROS architecture.

Finally, ROS launch files can be used to easily monitor, manage, and configure running nodes and services. Launch files can also be used to set global parameters before running and managing multiple nodes.

**ROS services are used to perform short-running tasks, such as reporting the goal summary. The service is defined in the file srv/GoalSummary.srv. The service server node is defined in the file src/goal_summary_server.py. The service client node is defined in the file src/goal_summary_client.py.**

-**ROS Action Servers**
The long-running tasks, such as robot planning and navigation, are handled by ROS action servers. The action server is defined in the file action/Goal.action. The action server node is defined in the file src/goal_action_server.py. The action client node is defined in the file src/goal_action_client.py.

-**Launch Files**
Launch files are utilized to set global parameters and manage multiple running nodes. The launch file is defined in the file launch/mylaunch.launch.

-----------------------------------------------------
## Installing and running
This assignment focuses on the development of a ROS package that utilizes the environmental simulation presented in the assignment_2_2022 package. Python nodes are written for the purpose of providing a way to interact with this environment, and the directory and CMakeList file were also modified. A launch file was developed in order to run the code.

In order to run the simulation, the following steps are required:

Install the assignment_2_2022 package by cloning the repository and building it with the catkin_make command.
Navigate to the assignment_2_2022/launch directory and launch the command roslaunch robot_sim mylaunch.launch
Monitor the 4 new terminal windows that shall appear:
The main terminal contains the roscore, services and action servers, as well as Gazebo and RViz
The second terminal shows a user-interface that allows the selection of positional goals for the robot or canceling them
The terminal window entitled kinematic data displays the robot's distance to target and average velocities along both the x and y axes
The goal-summary service prints the current number of reached or canceled goals of the robot.


In this section of the readme, we will cover how to install and run the robot_sim package.

First off, you will need to have ROS Noetic (ROS Noetic installation instructions) installed on your system. Once ROS has been installed you can execute the following commands in the terminal:

````shell
    roscore
    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws/
    catkin_make
    source ~/catkin_ws/devel/setup.bash
    cd ~/catkin_ws/src
````

Once done, you will be able to run the simulation as follows:

````shell
$ roslaunch rt1_project_2 project_2.launch

````
This will open up 4 terminal windows with a main terminal for running the roscore, services and action servers, gazebo, and rviz. Additionally, it will open a window for the user interface, show the kinematic data of the robot, such as the distance to target and average velocities in both x and y axes, and run a goal summary service so you can keep track of the goals the robot has achieved or canceled.