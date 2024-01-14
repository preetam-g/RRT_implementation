# This file contains all the functions, variables, objects, and their methods that will be used for implementation.
# I will be treating obstacles as circles of some fixed radius.

import turtle as tt  # using turtle for visualization
import math # calculations

# defining screen limits and other constants
HEIGHT = 700
WIDTH = 800
BUFF = int(WIDTH/15) # buffer to make sure they the random samples go out of the screen
OBS_RAD = 1.2 # used for obstacle size scaling 
NO_OF_OBS = 10 # number of obstacles on screen
STEP_MAX = 10 # max step distance in an iteration
SAFE = 25 # with OBS_RAD as 1.2, SAFE is the distance from center of obs where the obstacle will not collide with node.  

plotter = tt.Turtle() # used for plotting line
plotter.penup()
plotter.hideturtle()


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
        self.color("black")
        self.shapesize(stretch_len = OBS_RAD, stretch_wid = OBS_RAD)
        self.penup()
        self.hideturtle()

    def get_pos(self) -> tuple:
        return (self.xcor(), self.ycor())

    def start_goal_safe(self, start_node_loc: tuple, goal_node_loc: tuple) -> bool:
        
        if distance(start_node_loc, self.get_pos()) < SAFE: return False
        elif distance(goal_node_loc, self.get_pos()) < SAFE: return False
        
        return True


class Node(tt.Turtle):

    def __init__(self, position: tuple):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len = 0.8, stretch_wid = 0.8)
        self.penup()
        self.goto(position[0], position[1])
    
    parent = 0
    def parent(self, node_parent) -> tuple:
        parent = node_parent
        return node_parent


    def get_pos(self) -> tuple:
        return (self.xcor(), self.ycor())
    
    def get_nearest_node(self, nodes: list):
        
        dist = math.inf
        res = None
        
        for node in nodes:
            temp = distance(self.get_pos(), node.get_pos())
            if temp < dist: 
                res = node
                dist = temp
        
        return res
    
    def extend_toward(self, node_rand: tuple):
        # returns location of next node to be connected to nearest node
        
        theta = math.atan2((node_rand.ycor() - self.ycor()), (node_rand.xcor() - self.xcor()))
        new_x = self.xcor() + 2*math.cos(theta)*STEP_MAX
        new_y = self.ycor() + 2*math.sin(theta)*STEP_MAX
        
        plotter.goto(self.get_pos())
        plotter.pd()
        plotter.goto((new_x, new_y))
        plotter.pu()

        return (new_x, new_y)
    
def goal_found(goal , all_nodes: list) -> bool:
    near_goal = goal.get_nearest_node(all_nodes)
    if distance(near_goal.get_pos(), goal.get_pos()) < STEP_MAX: return True
    else: return False