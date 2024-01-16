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
drive_motors = MotorGroup(left_motor, right_motor)
drive_motors.set_velocity(150, RPM)
# moving both motors at the same time
drive_motors.spin_for(FORWARD, 360*5, DEGREES)
# moving one after another
left_motor.spin_for(FORWARD, 360*5, DEGREES)
right_motor.spin_for(FORWARD, 360*5, DEGREES)
