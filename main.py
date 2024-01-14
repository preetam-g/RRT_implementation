import objects as obj 
import turtle as tt
import random, time

IN = lambda type = int:tuple(map(type, input().split()))

screen = tt.Screen()
screen.title("RRT_implementation")
screen.setup(width = obj.WIDTH, height = obj.HEIGHT)
screen.tracer(0) # refreshes screen only when screen.update() is used

start_node = IN()
end_node = IN()

stones = [] # list that stores the obstacles and their locations
while len(stones) < (obj.NO_OF_OBS):

    temp = obj.Obstacle() # temporary obstacle variable
    randx = random.choice(range(-obj.WIDTH//2 + obj.BUFF, obj.WIDTH//2 - obj.BUFF)) # assigning random locations for obstacles
    randy = random.choice(range(-obj.HEIGHT//2 + obj.BUFF, obj.HEIGHT//2 - obj.BUFF))
    # add a line to make sure obstacles don't collide with start and goal 
    if temp.start_goal_safe(): 
        temp.goto(randx, randy)
        stones.append((temp, randx, randy))
    screen.update()
    time.sleep(5)



screen.exitonclick()