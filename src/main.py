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
brain.screen.print("Hello World 2")

left_motor = Motor(Ports.PORT1, 0.2, True)
right_motor = Motor(Ports.PORT10, 0.2, False)
arm_motor = Motor(Ports.PORT8, 0.2, True) # take a look at params for validity
button = Bumper(brain.three_wire_port.d)
range_finder = Sonar(brain.three_wire_port.e)

drive_motors = MotorGroup(left_motor, right_motor)



arm_motor.set_velocity(150)

def driveOn() -> None:
	arm_motor.spin_for(FORWARD, 120, DEGREES) # TODO: test
	drive_motors.set_velocity(150)
	drive_motors.spin(FORWARD)
	while range_finder.distance(MM) > 200 and range_finder.distance(MM) < 5: # TODO: test
		# keep spinning
		continue
	drive_motors.set_velocity(100)
	while range_finder.distance(MM) > 100 and range_finder.distance(MM) < 5: # TODO: test
		# keep spinning
		continue
	drive_motors.set_velocity(50)
	while range_finder.distance(MM) > 50 and range_finder.distance(MM) < 5: # TODO: test
		# keep spinning
		continue
	drive_motors.stop()
	arm_motor.spin_for(REVERSE, 75, DEGREES)  # TODO: test
	brain.screen.print(arm_motor.torque())

button.pressed(driveOn)
