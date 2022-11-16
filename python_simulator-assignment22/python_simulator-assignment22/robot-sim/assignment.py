from __future__ import print_function

import time
import random
from sr.robot import *

"""
Exercise 2 python script

Put the main code after the definition of the functions. The code should make the robot grab the closest marker (token)
Steps to be performed:
1 - call the function find_token() to retrieve the distance and the angle between the robot and the closest marker
2 - drive the robot towards the marker. If the distance between the robot and the marker is less than d_th
     meters, the robot can grab the marker, by using the method grab() of the class Robot. Otherwise, the 
     robot should be driven toward the token. The robot is a non-holonomic robot, so you should control the 
     angle, by calling the method turn, if rot_y is greater then a_th or lower then -a_th (check the sign!).
     On the contrary, if -a_th < rot_y < a_th, you can use the method drive to move the robot forward.
3 - after you grab the marker, you can exit the program (function exit()).

   When done, run with:
	$ python run.py solutions/exercise2_solution.py
"""


a_th = 2.0
flag_robot_state=0;
""" float: Threshold for the control of the linear distance"""

d_th = 0.8
""" float: Threshold for the control of the orientation"""

R = Robot()
""" instance of the class Robot"""


def drive(speed, seconds):
    """
    Function for setting a linear velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    speed=speed*5
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

def turn(speed, seconds):
    """
    Function for setting an angular velocity
    
    Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
    """
    R.motors[0].m0.power = speed
    R.motors[0].m1.power = -speed
    time.sleep(seconds)
    R.motors[0].m0.power = 0
    R.motors[0].m1.power = 0

# My_Solution =======================================================================================

def find_silver():
	dist =100
	for token in R.see():
		#print(token)
		if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER: # found a silver token
			print("found a silver token!")
			dist=token.dist
			rot_y=token.rot_y
	if dist==100:
		return -1, -1
        else:
   		return dist, rot_y
   		
def find_gold():
	dist =100
	for token in R.see():
	#print(token)
		if token.dist < dist and token.info.marker_type is MARKER_TOKEN_GOLD: # found a gold token
			print("found a golden token!")
			dist=token.dist
			rot_y=token.rot_y
	if dist==100:
		return -1, -1
        else:
   		return dist, rot_y
   		
def go_to_goal(obj_dis,obj_rot):
	flag_robot_state = 0;
	if obj_dis <0.4:
		flag_robot_state = 1
		test=R.grab() 			# if we are close to the token, we grab it.
		print("Found it!")
		print("Gotcha!") 
		return flag_robot_state	
	elif -a_th<= obj_rot <= a_th: 		# if the robot is well aligned with the token, we go forward
		print("Ah, here we are!.")
		drive(10, 0.5)
	elif obj_rot < -a_th: 			# if the robot is not well aligned with the token, we move it on the left or on the right
		print("Left a bit...")
		turn(-2, 0.5)
	elif obj_rot > a_th:
		print("Right a bit...")
		turn(+2, 0.5)

	return flag_robot_state



while 1:
#hyperparameter
	step_degree_Silver=3
	step_degree_Gold=3
	
	
	dist_silver,rot_silver = find_silver() # I look for silver markers
	if dist_silver == -1:
		while 1:
			dist_silver,rot_silver = find_silver()
			turn(step_degree_Silver,1)
			#drive(-10, 0.5) 
			if dist_silver>0:
				break
			else:
				print(flag_robot_state)
				print("Robot Can not fine the silver Box")
	
	if flag_robot_state == 0:
		flag_robot_state = go_to_goal(dist_silver,rot_silver)
		
	elif flag_robot_state == 1:
		while 1:
			print("Mission Start")
		
			dist_gold,rot_gold = find_gold()
			if dist_gold == -1:
				while 1:
					dist_gold,rot_gold = find_gold()
					turn(step_degree_Gold,1)
					#drive(-10, 0.5) 
					if dist_gold > 0:
						break
					else:
						print("Robot Can not fine the Gold Box")
						#exit()  # if no markers are detected, the program ends
				
			
			go_to_goal(dist_gold,rot_gold)
			
			if dist_gold <d_th:
				print("rich to Goal")
				R.release()
				drive(-10, 1) 
				#turn(8+random.randint(0,8),5)
				flag_robot_state = 0
			break
				
		      

       
       

	
