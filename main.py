# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       pbeau                                                        #
# 	Created:      1/14/2024, 6:17:53 PM                                        #
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
left_motor.spin(FORWARD, 2.5, RPM)
right_motor.spin(FORWARD, 2.5, RPM)


        
