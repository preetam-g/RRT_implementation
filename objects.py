# This file contains all the functions, variables, objects, and their methods that will be used for implementation.
# I will be treating obstacles as circles of some fixed radius.

import turtle as tt  # using turtle for visualization
import math # calculations
import random # selectinng random location on coordinate plane

# defining screen limits and other constants
HEIGHT = 600
WIDTH = 600
BUFF = int(WIDTH/10) # buffer to make sure they the random samples go out of the screen
OBS_RAD = 1.2 # used for obstacle size scaling 
NO_OF_OBS = 1 # number of obstacles on screen
STEP_MAX = 10 # max step distance in an iteration
SAFE = 25 # with OBS_RAD as 1.2, SAFE is the distance from center of obs where the obstacle will not collide with node.  


class Obstacle(tt.Turtle): # creating obstacle object which is child of turtle class in turtle module.

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len = OBS_RAD, stretch_wid = OBS_RAD)
        self.penup()

class Node(tt.turtle):

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()

    def get_pos(self) -> tuple:
        return (self.xcor(), self.ycor())