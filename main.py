import objects as obj 
import turtle as tt
import random, time
import math

IN = lambda type = int:tuple(map(type, input().split()))

screen = tt.Screen()
screen.title("RRT_implementation")
screen.setup(width = obj.WIDTH, height = obj.HEIGHT)
screen.tracer(0) # refreshes screen only when screen.update() is used


start_loc = (-200, -200)
end_loc = (200, 200)

stones = [] # list that stores the obstacles objects

print("How do you want your arena? 1: preset, 2: random, 3: you can set everything manually.")
generated = False
decide_obs = input("choose (1, 2, 3): ")
while not generated:

    if decide_obs == '1':  

        stones = [obj.Obstacle((0, 0)), obj.Obstacle((20, -20)), obj.Obstacle((-20, 20)), obj.Obstacle((20, 20)), obj.Obstacle((170, 160)), obj.Obstacle((100, 150)), obj.Obstacle((-35, 35)), obj.Obstacle((35, -35)), obj.Obstacle((50, -50)), obj.Obstacle((-50, 50)), obj.Obstacle((-60, 60)), obj.Obstacle((start_loc[0]+30, start_loc[1]+35))] 

        generated = True

    elif decide_obs == '2':

        # random start, end locations
        start_loc = tuple(random.sample(range(-obj.WIDTH//2 + 2*obj.BUFF, obj.WIDTH//2 - 2*obj.BUFF), 2))
        end_loc = tuple(random.sample(range(-obj.HEIGHT//2 + 2*obj.BUFF, obj.HEIGHT//2 - 2*obj.BUFF), 2))

        # random obstacles
        while len(stones) < obj.NO_OF_OBS:

            # temporary obstacle variable
            randx = random.choice(range(-obj.WIDTH//2 + obj.BUFF, obj.WIDTH//2 - obj.BUFF)) # assigning random locations for obstacles
            randy = random.choice(range(-obj.HEIGHT//2 + obj.BUFF, obj.HEIGHT//2 - obj.BUFF))

            temp = obj.Obstacle((randx, randy))
            if temp.start_goal_safe(start_loc, end_loc): 
                stones.append(temp)
                temp.showturtle()
            
            generated = True

    elif decide_obs == '3':

        print(f"give coordinates of start node, x then y both absolute value less than {min(obj.HEIGHT, obj.WIDTH)*0.4}:", end = " ")
        start_loc = IN()
        print(f"similarly for end location:", end = " ")
        end_loc = IN()

        num = int(input("give num of obstacles you want?:"))
        print(f"give location x then y in absolute value less than {min(obj.HEIGHT, obj.WIDTH)*0.4} seperated with spaces: ")
        for x in range(num):
            print(f"obstacle {x+1}:", end = " ")
            place = IN()
            temp = obj.Obstacle(place)
            if temp.start_goal_safe(start_loc, end_loc): 
                stones.append(temp)
                temp.showturtle()
        
        generated = True

    else: 
        print('choose correctly:', end = " ")
    
    screen.update()

# creating start and end node on screen
start_point = obj.Node(start_loc)
start_point.color("yellow") # blue for start node
start_point.shapesize(stretch_len = 1.2, stretch_wid = 1.2)
start_point.set_parent(start_point)

end_point = obj.Node(end_loc)
end_point.color("green") # green for end node
end_point.shapesize(stretch_len = 1.2, stretch_wid = 1.2)

nodes = [start_point]
x = 0
# x_start = min(start_loc[1], end_loc[1])
# x_end = max(start_loc[1], end_loc[1])
# y_start = min(start_loc[1], end_loc[1])
# y_end =  max(start_loc[1], end_loc[1])

# rrt node generation and path creation
while not obj.goal_found(end_point, nodes):
    
    # randx = random.choice(range( x_start, x_end )) # assigning random locations for obstacles
    # randy = random.choice(range( y_start, y_end ))
   
    # generating random node in the 180 degree arc of nearest node for goal point
    n_node = end_point.get_nearest_node(nodes)
    x, y = n_node.get_pos() 
    goal_to_node_theta = math.atan2((end_loc[1] - y), (end_loc[0] - x))
    theta_range = random.uniform(-1, 1)
    theta_delta = math.pi*0.5
    theta = goal_to_node_theta + theta_range*theta_delta
    dist = obj.distance((x, y), end_loc)*0.75
    randx, randy = x + math.cos(theta)*dist, y + math.sin(theta)*dist

    if x%5 == 0: randx, randy = end_loc # this is to bias the tree towards goal point
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
        new_node.set_parent(nearest_node)
        nodes.append(new_node)
    
    time.sleep(0.1)
    screen.update()
    x += 1




screen.exitonclick()