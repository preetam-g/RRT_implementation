import objects as obj 
import turtle as tt
import random, time

screen = tt.Screen()
screen.title("RRT_implementation")
screen.setup(width = obj.WIDTH, height = obj.HEIGHT)
screen.tracer(0) # refreshes screen only when screen.update() is used


stones = []
for x in range(obj.NO_OF_OBS):

    temp = obj.Obstacle() # temporary obstacle variable
    randx = random.choice(range(-obj.WIDTH//2 - obj.BUFF, obj.WIDTH//2 - obj.BUFF)) # assigning random locations for obstacles
    randy = random.choice(range(-obj.HEIGHT//2 - obj.BUFF, obj.HEIGHT//2 - obj.BUFF))
    temp.goto(randx, randy)
    stones.append((temp, randx, randy))
    screen.update()



screen.exitonclick()