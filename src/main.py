# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       ritvi                                                        #
# 	Created:      1/15/2024, 12:03:14 PM                                       #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# The controller
controller = Controller()
# Brain should be defined by default
brain = Brain()

left_motor = Motor(Ports.PORT1, 0.2, True)
right_motor = Motor(Ports.PORT10, 0.2, False)
arm_motor = Motor(Ports.PORT8, 0.2, True) # take a look at params for validity
button = Bumper(brain.three_wire_port.d)
range_finder = Sonar(brain.three_wire_port.e) # NOTE: has a range of 30 to 3000 MM

drive_motors = MotorGroup(left_motor, right_motor)

arm_motor.set_velocity(150)

num_trials = 30

def addValue(arr, val):
	newArr = arr
	if len(arr) == 0:
		newArr.append(val)
	elif len(arr) < num_trials:
		for i in range(len(arr) - 1):
			newArr[i+1] = arr[i]
		newArr[0] = val
		newArr.append(arr[len(arr) - 1])
	else:
		for i in range(num_trials - 1):
			newArr[i+1] = arr[i]
		newArr[0] = val
	return newArr

def check_change(trials, acc, max_val, min_val) -> bool:
	if len(trials) < num_trials / 2:
		return True
	total_correct = 0.0
	for i in range(len(trials)):
		trial = trials[i]
		if trial < max_val and trial > min_val:
			total_correct += 1
	return total_correct / len(trials) < acc

def drive() -> None:
	brain.screen.clear_screen()
	arm_motor.spin_for(FORWARD, 143*5, DEGREES)
	drive_motors.set_velocity(150, RPM)
	drive_motors.spin(FORWARD)
	distance_trials = [] # has latest num_trials values the range finder has given, with the most recent being in index 0
	accuracy = 0.9
	brain.screen.print_at("150 RPM", x=50, y=100)
	while check_change(distance_trials, accuracy, 400, 35):
		distance_trials = addValue(distance_trials, range_finder.distance(MM))
		# keep spinning
		brain.screen.clear_line()
		brain.screen.print_at(distance_trials[0], x=50, y=50)
	drive_motors.set_velocity(100, RPM)
	brain.screen.print_at("100 RPM", x=50, y=100)
	while check_change(distance_trials, accuracy, 175, 35):
		distance_trials = addValue(distance_trials, range_finder.distance(MM))
		# keep spinning
		brain.screen.clear_line();
		brain.screen.print_at(distance_trials[0], x=50, y=50)
	drive_motors.set_velocity(50, RPM)
	brain.screen.print_at("50 RPM ", x=50, y=100)
	while check_change(distance_trials, accuracy, 90, 35):
		distance_trials = addValue(distance_trials, range_finder.distance(MM))
		# keep spinning
		brain.screen.clear_line();
		brain.screen.print_at(distance_trials[0], x=50, y=50)
		wait(100)
	drive_motors.stop()
	brain.screen.clear_screen()
	brain.screen.print_at("Stopped", x=50, y=100)
	arm_motor.spin_for(REVERSE, 28*5, DEGREES)
	while True:
		brain.screen.print_at(arm_motor.torque(), x=50, y=50)

# boot up range finder
for i in range(10):
	brain.screen.print_at(range_finder.distance(MM), x=50, y=50)
	wait(100)
brain.screen.clear_screen()
brain.screen.print_at("Button Active", x=50, y=50)
button.pressed(drive)
