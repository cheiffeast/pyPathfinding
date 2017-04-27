import AI
import Map
import misc
import pygame
from pygame.locals import *
import numpy as np

def simple():
    screen = pygame.display.set_mode([500, 500])
    a = Map(screen, size = [25, 25])
    path = a.Astar()
    while 1:
        a.draw()
        for item in path:
            pygame.draw.rect(screen, [0, 255, 0], [item[0] * a.cellsize[0], item[1] * a.cellsize[1], a.cellsize[0], a.cellsize[1]])
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        m = pygame.mouse.get_pressed()
        if m[0]:
            mpos = pygame.mouse.get_pos()
            loc = [int(mpos[0] / a.cellsize[0]), int(mpos[1] / a.cellsize[1])]
            a.walls[loc[0]][loc[1]] = 1
            path = a.Astar()
            print(path[-1])
        pygame.display.update()

def aiexample():
    screen = pygame.display.set_mode([500, 500])
    map1 = Map.Map(screen, size = [20, 20], walls = [[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [6, 0], [6, 1]])
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

        pygame.display.update()
aiexample()