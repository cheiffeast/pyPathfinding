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
# Documentation
## Map
In this implementation of A* search I have used a Map object to store the walls and calulate the shorest route in. In doing so the main loop of the game/demo can be alot smaller as 50 lines of code can be expressed in 1 line. The below bulletpoints breifly describe what each function does
* __init__ - The init function is run when the object is initalised and for the Map object you can pass multiple parameters
    * surface - This is the [pygame surface](https://www.pygame.org/docs/ref/surface.html) that you want to draw the Map onto. (Required)
    * size - This is the width and the height of the Map in cells. Format = [width, height]. Default = [10, 10]
    * walls: This is a list of walls that are to be made when the Map is initalised. Format = [[wallxpos, wallypos]] where wallxpos is the x coordinate in cells (not pixels) and wallypos is the y coordinate in cells. Default = []
* __getneibs__ - This function is used to get the neighbours of a position, also checks if there is a wall there and will not return a cell tht is a wall
    * currentpos - This is the current position you wish to get the neighbours of. Format = [x, y] where x and y are cell position (not pixe). (Required)
* __Astar__ - This is the function that calculates the shorest route between 2 positions taking into account the walls in the Map
    * startpos - This is the position you want to start the solution from. Format = (x, y) where x and y are cell position (not pixels). Default = (0, 0)
    * endpos - This is the position you want to end the solution to. Format = (x, y) where x and y are cell positions (not pixels). Default = (). If left default it will solve to the bottom right corner of the Map
* __reconstruct__ - This is a function to reconstruct the A* solution path
    * current - This is the position of the current position the A* algorithm is looking at when it finds the best solution, should be end point. Format = (x, y) x and y are cell positions (not pixels)
    * camefrom - A dictionary that allows you to span back up to the original start point. Traverse up to the start position hence returning the shortest path. Format = {}
    * startpos - The start position from the __Astar__ function, this is used to check if we have reached the end point. Format = [x, y] where x and y are cell positions (not pixels). Default = [0, 0]
* __draw__ - This is the function to draw the Map to the surface specified in the __init__. Draws walls as black, none walls as white

    
    
