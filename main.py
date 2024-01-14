import objects as obj 
import turtle as tt
import random, time

IN = lambda type = int:tuple(map(type, input().split()))

screen = tt.Screen()
screen.title("RRT_implementation")
screen.setup(width = obj.WIDTH, height = obj.HEIGHT)
screen.tracer(0) # refreshes screen only when screen.update() is used

print("give coordinates of start node:", end = " ")
start_loc = IN()
print("give coordinates of start node:", end = " ")
end_loc = IN()

# creating start and end node on screen
# start_point = obj.Node(start_loc)
# end_point = obj.Node(end_loc)

stones = [] # list that stores the obstacles and their locations as tuples (obj, xcor, ycor)
for x in range(obj.NO_OF_OBS + 3):

    temp = obj.Obstacle() # temporary obstacle variable
    randx = random.choice(range(-obj.WIDTH//2 + obj.BUFF, obj.WIDTH//2 - obj.BUFF)) # assigning random locations for obstacles
    randy = random.choice(range(-obj.HEIGHT//2 + obj.BUFF, obj.HEIGHT//2 - obj.BUFF))

    if temp.start_goal_safe(start_loc, end_loc): 
        temp.goto(randx, randy)
        stones.append((temp, randx, randy))

    screen.update()
    # time.sleep(1)

# nodes = []
# for x in range(10):
#     randx = random.choice(range(-obj.WIDTH//2 + obj.BUFF, obj.WIDTH//2 - obj.BUFF)) # assigning random locations for obstacles
#     randy = random.choice(range(-obj.HEIGHT//2 + obj.BUFF, obj.HEIGHT//2 - obj.BUFF))
#     temp = obj.Node((randx, randy))
#     nodes.append((temp, randx, randy))
#     screen.update()


screen.exitonclick()