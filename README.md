# pyPathfinding
pyPathfinding is a project that shows and builds on how the A* algorithm works and can be implemented into games easily. To run the examples download the repository and open examples.py, uncomment the example you want to use and run examples.py. The gif below shows the simple() in examples.py at work.

<p align = "center">
<img src = "http://i.imgur.com/OQTjAnl.gif" align = "middle"/>
</p>


# Examples
There are already 2 pre-built examples of how you can use A* to allow AI to nagivate through a map. Another example shows how A star can be done in real time by allowing you to place walls and the algorithm will update itself
Examples:
1. simple - Simple is a simple useage of A* that allows the placing and walls and updating the A star solution upon doing so. To run uncomment simple() at the bottom of examples.py
2. aiexample - Aiexmaple is a function that uses the AI.py file that allows a AI to find a path to a position and wander around the map in a roi (region of interest). To run aiexample uncomment aiexmaple() at the bottom of the examples.py file

# Map
In this implementation of A* search I have used a Map object to store the walls and calulate the shorest route in. In doing so the main loop of the game/demo can be alot smaller as 50 lines of code can be expressed in 1 line. The below bulletpoints breifly describe what each function does
* __init__ - The init function is run when the object is initalised and for the Map object you can pass multiple parameters
           - surface: This is the [pygame surface](https://www.pygame.org/docs/ref/surface.html) that you want to draw the Map onto
