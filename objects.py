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

def distance(pos1: tuple, pos2: tuple) -> float:
    x1, y1 = pos1
    x2, y2 = pos2
    xdis = (x1 - x2)**2
    ydis = (y1 - y2)**2
    return math.sqrt(xdis + ydis)

class Obstacle(tt.Turtle): # creating obstacle object which is child of turtle class in turtle module.

    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len = OBS_RAD, stretch_wid = OBS_RAD)
        self.penup()

    def get_pos(self) -> tuple:
        return (self.xcor(), self.ycor())

    def start_goal_safe(self, start_node: tuple, goal_node: tuple) -> bool:
        
        if distance(start_node, self.get_pos()) <= SAFE: return False
        elif distance(goal_node, self.get_pos()) <= SAFE: return False
        
        return True


class Node(tt.turtle):

    def __init__(self, position: tuple) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(position[0], position[1])

    def get_pos(self) -> tuple:
        return (self.xcor(), self.ycor())