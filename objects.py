# This file contains all the functions, variables, objects, and their methods that will be used for implementation.
# I will be treating obstacles as circles of some fixed radius.

import turtle as tt  # using turtle for visualization
import math # calculations
import random # selectinng random location on coordinate plane

# defining screen limits and other constants
HEIGHT = 800
WIDTH = 1000
BUFF = int(WIDTH/10) # buffer to make sure they the random samples go out of the screen
OBS_RAD = 10 # obstacle radius 
STEP_max = 10 # max step distance in an iteration
