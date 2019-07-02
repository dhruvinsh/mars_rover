[![Build Status](https://travis-ci.org/dhruvinsh/mars_rover.svg?branch=master)](https://travis-ci.org/dhruvinsh/mars_rover)
[![codecov](https://codecov.io/gh/dhruvinsh/mars_rover/branch/master/graph/badge.svg)](https://codecov.io/gh/dhruvinsh/mars_rover)


# MARS ROVERS 
Aim of this project is to resolve below task.

# Task
A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth. 
 
A rover's position and location is represented by a combination of x and y coordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North. 
 
In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M' means move forward one grid point, and maintain the same heading. 
 
Assume that the square directly North from (x, y) is (x, y+1). 
 
Write a program that takes in instructions for the rovers’ movements and prints out their final positions. 
 
INPUT: The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0. 
 
The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau. 
 
The position is made up of two integers and a letter separated by spaces, corresponding to the x and y coordinates and the rover's orientation. 
 
Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving. 
 
OUTPUT The output for each rover should be its final coordinates and heading. 
 
INPUT AND OUTPUT 
 
``` text
Test Input:
5 5

1 2 N
LMLMLMLMM

3 3 E
MMRMMRMRRM
 
Expected Output:
1 3 N
5 1 E
```

# Brainstorming

As seen from above task and input data, we can say that, problem revolve around coordinates and angles(directions). Lets take an example of below input data,

``` text
5 5

1 2 N
LMLMLMLMM
```

Mars Rover is, surprisingly on rectangular plateau. The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.
From the first line, we can say that plateau size is 5 x 5 (x axis- 0 to 5 and y axis 0 to 5). Second line is rover's location. So origin for rower is `(1, 2)` and facing north.

We can divide directions in angles with respect to North as below,
``` text
                     0 degrees
                      North
                        ^
                        |
                        |
                        |
270 degrees - West <----|----> East - 90 degrees
                        |
                        |
                        |
                        v
                      South
                   180 degrees
```

So rover's origin is `(1, 2, 0)` where x-axis=1, y-axis=2 and direction=0 degrees.

if the rover take right turn we will add position 90 degrees to it, else on left turn we will add negative 90 degrees to existing. and for given mover forward command we will add unit component of the same direction. Different direction addition is not implemented by default. See below image for rover's movement for above exampled input data.

![Rover](assets\rover.png "Rover movement")
