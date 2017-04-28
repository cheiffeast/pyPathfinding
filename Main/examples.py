import pygame
from pygame.locals import *

import AI
import Map


def simple():
    # Setting up the pygame surface and clock
    screen, clock = pygame.display.set_mode([500, 500]), pygame.time.Clock()
    # Creating the map object and solving a A star route from the top left corner to bottom right (default)
    map = Map.Map(screen, size = [30, 30])
    path = map.Astar()
    playing = True
    # Main game loop
    while playing:
        # Do drawing of the map and of the A star solution path
        map.draw()
        for item in path:
            pygame.draw.rect(screen, [0, 255, 0],
                            [item[0] * map.cellsize[0],
                            item[1] * map.cellsize[1],
                            map.cellsize[0], map.cellsize[1]])
        # Pygame event loop that allows user to quit from the loop
        for event in pygame.event.get():
            if event.type == QUIT:
                playing = False
        # Checking if the mouse button 1 is currently pressed or not
        # pygame.mouse.get_pressed() gets the buttons on the mouse that are pressed
        mousePressed = pygame.mouse.get_pressed()
        if mousePressed[0]:
            # Find where the user is clicking and translate into cell in the map. Set that cell to 1 (wall)
            mousePosition = pygame.mouse.get_pos()
            map.walls[int(mousePosition[0] / map.cellsize[0]), int(mousePosition[1] / map.cellsize[1])] = 1
            # Recreate the A star solution path
            path = map.Astar()

        # Update the python surface and make sure the FPS is less than or equal to 60
        pygame.display.update()
        clock.tick(60)
    pygame.quit()

def aiexample():
    screen = pygame.display.set_mode([500, 500])
    map1 = Map.Map(screen, size = [20, 20], walls = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [6, 0], [6, 1]])
    clock = pygame.time.Clock()
    ai = AI.AI(map1)
    ai.moveto([15, 15])

    while 1:
        screen.fill([255, 255, 255])
        map1.draw()
        ai.move()
        pygame.draw.rect(screen, [0, 255, 0], [ai.currentpos[0] * map1.cellsize[0], ai.currentpos[1] * map1.cellsize[1], map1.cellsize[0], map1.cellsize[1]])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                mpos = pygame.mouse.get_pos()
                loc = [int(mpos[0] / map1.cellsize[0]), int(mpos[1] / map1.cellsize[1])]
                ai.moveto(loc)
        pygame.display.update()
        clock.tick(60)

#simple()
#aiexample()