import objects as obj 
import turtle as tt
import random, time
import math

IN = lambda type = int:tuple(map(type, input().split()))

screen = tt.Screen()
screen.title("RRT_implementation")
screen.setup(width = obj.WIDTH, height = obj.HEIGHT)
screen.tracer(0) # refreshes screen only when screen.update() is used


# print(f"give coordinates of start node, x then y both abs value less than {min()}:", end = " ")
# start_loc = IN()
# print(f"give coordinates of start node, x then y both in range(-300, 300):", end = " ")
# end_loc = IN()

start_loc = (-200, -200)
end_loc = (200, 200)



# creating start and end node on screen
start_point = obj.Node(start_loc)
start_point.color("yellow") # blue for start node
start_point.shapesize(stretch_len = 1.2, stretch_wid = 1.2)
start_point.parent(start_point)
end_point = obj.Node(end_loc)
end_point.color("green") # green for end node

stones = [obj.Obstacle((0, 0)), obj.Obstacle((20, -20)), obj.Obstacle((-20, 20)), obj.Obstacle((20, 20)), obj.Obstacle((170, 160)), obj.Obstacle((100, 150))] # list that stores the obstacles objects
# while len(stones) < obj.NO_OF_OBS:

#     temp = obj.Obstacle() # temporary obstacle variable
#     randx = random.choice(range(-obj.WIDTH//2 + obj.BUFF, obj.WIDTH//2 - obj.BUFF)) # assigning random locations for obstacles
#     randy = random.choice(range(-obj.HEIGHT//2 + obj.BUFF, obj.HEIGHT//2 - obj.BUFF))
    
#     temp.goto(randx, randy)
#     if temp.start_goal_safe(start_loc, end_loc): 
#         stones.append(temp)
#         temp.showturtle()

#     screen.update()
#     # time.sleep(0.4)

nodes = [start_point]
x = 0
while not obj.goal_found(end_point, nodes):

    if x%5 == 0: 
        temp = obj.Node(end_loc)
        temp.hideturtle()
    else:
        # randx = random.choice(range( min(start_loc[1], end_loc[1]), max(start_loc[1], end_loc[1]) )) # assigning random locations for obstacles
        # randy = random.choice(range( min(start_loc[1], end_loc[1]), max(start_loc[1], end_loc[1]) ))
        x, y = end_point.get_nearest_node(nodes).get_pos()
        goal_to_node_theta = math.atan2((end_loc[1] - y), (end_loc[0] - x))

        theta_range = random.uniform(-1, 1)
        theta_delta = math.pi
        theta = goal_to_node_theta + theta_range*theta_delta
        
        randx, randy = x + math.cos(theta)*obj.STEP_MAX*3, y + math.sin(theta)*obj.STEP_MAX*3 
        temp = obj.Node((randx, randy))

    temp.color("red")
    temp.shapesize(stretch_len = 0.15, stretch_wid = 0.15)

    # find nearest node and increase step, check obstacle
    nearest_node = temp.get_nearest_node(nodes)
    path = True
    for stone in stones: 
        if not nearest_node.path_exists(stone, temp): 
            path = False

    
    if path: 
        x, y  = nearest_node.extend_toward(temp)
        new_node = obj.Node((x, y))
        new_node.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        new_node.parent(nearest_node)
        nodes.append(new_node)
    
    time.sleep(0.4)
    screen.update()
    x += 1


screen.exitonclick()