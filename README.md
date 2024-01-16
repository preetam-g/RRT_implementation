# RRT_implementation
Implementing an autonomous robotic path planning algorithm namely Rapidly exploring random tree(RRT). Used in simple obstacle modeling of the space and helps in path planning of wheeled robots.

# Obstacles, start and end points
Obstacles are treated as circles centered at a given location on the screen. 
I have not added any method to add obstacles manually, for testing purposes I have set fixed start, end points and obstacles in between them. I have commented out the code where we can input start and end location. I have also written code for random obstacle generation which can be replaced with manually addition later on if required.

# Modules used 
Turtle module of python has been used for visualization of the simulation. 
Time module has been used to slow down the simulation in order to see the expansion of tree. 
Random module has been used to generate random locations for obstacles, start, end locations.

# Concepts 
Classes have been used to create obstacle class and node class. These classes are child classes of "Turtle" class in turtle module.
Attributes and Methods have been defined based on requirement of the algorithm. 

# How to run code
Make sure the main.py and objects.py are in the same directory before running the program.
In terminal, move to the directory you have saved the files in. 
Then use command "python3 main.py" if it's ubuntu or use "python main.py" if it's VS Code.
There are 3 options on how to run the code. 
**Option 1:** Everything is preset.
**Option 2:** Everything will be randomly generated.
**Option 3:** You can manually set all the variables.
If you choose option 3, note that the center of the screen is origin and the screen will be divided into 4 quadrants. 

# Test results
![test_result_1](https://github.com/preetam-g/RRT_implementation/assets/118665778/3941af10-0776-42f8-bc34-6d97cf170b61)
![test_result_2](https://github.com/preetam-g/RRT_implementation/assets/118665778/416bbf56-d64e-4586-9471-a540d8b979cd)
![test_result_3](https://github.com/preetam-g/RRT_implementation/assets/118665778/327294b0-fa7a-4387-8008-5c80713f3c64)
![test_result_4](https://github.com/preetam-g/RRT_implementation/assets/118665778/b7734679-77c0-4903-ae26-20b47d6c7d17)
