import misc
import pygame
import numpy as np
from pygame.locals import *




class Map():
    def __init__(self, surface, size = [10, 10], walls = []):
        self.surface = surface
        self.surfsize = surface.get_size()
        self.cellsize = [self.surfsize[0] / size[0], self.surfsize[1] / size[1]]
        self.size = size
        self.walls = np.zeros(size)
        for wall in walls:
            self.walls[wall[0]][wall[1]] = 1

    def draw(self):
        self.surface.fill([255, 255, 255])
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.walls[x][y]:
                    pygame.draw.rect(self.surface, [0, 0, 0], [self.cellsize[0] * x,
                                                               self.cellsize[1] * y,
                                                               self.cellsize[0],
                                                               self.cellsize[1]])

    def getneibs(self, currentpos):
        neibs_ = [[currentpos[0] - 1, currentpos[1]],
                 [currentpos[0], currentpos[1] - 1],
                 [currentpos[0] + 1, currentpos[1]],
                 [currentpos[0], currentpos[1] + 1]]
        neibs = []
        for neib in neibs_:
            if neib[0] > -1 and neib[0] < self.size[0]:
                if neib[1] > -1 and neib[1] < self.size[1]:
                    if int(self.walls[neib[0]][neib[1]]) == 0:
                        neibs.append(neib)
        return neibs

    def depthfirst(self, startpos=[0, 0]):
        endpos = np.array(self.size) - 1
        stack = []
        path = []
        visited = np.zeros(self.size)
        visited[startpos[0]][startpos[1]] = 1
        currpos = startpos
        while list(currpos) != list(endpos):
            neibs_ = self.getneibs(currpos)
            neibs = []
            for neib in neibs_:
                if int(visited[neib[0]][neib[1]]) == 0:
                    neibs.append(neib)
            if len(neibs) == 0:
                currpos = stack.pop(0)
                path.pop(-1)
            else:
                neibd = []
                for neib in neibs:
                    neibd.append([misc.dist_between(neib, endpos), neib])
                neibd = sorted(neibd)
                stack.insert(0, currpos)
                currpos = neibd[0][1]
                visited[currpos[0]][currpos[1]] = 1
                path.append(currpos)
        return path

    def Astar(self, startpos = [0, 0], endpos = []):
        gscore = np.empty(self.size)
        gscore[startpos[0]][startpos[1]] = 0
        fscore = np.empty(self.size)
        open = [startpos]
        closed = []
        camefrom = np.empty(self.size + [2,])
        if len(endpos) == 0:
            endpos = [self.size[0] - 1, self.size[1] - 1]
        while len(open):
            current = sorted([[fscore[cell[0]][cell[1]], cell] for cell in open])[0][1]
            if current == endpos:
                print("here")
                return self.reconstruct(camefrom, current)

            open.pop(open.index(current))
            closed.append(current)

            for neib in self.getneibs(current):
                if neib in closed:
                    continue

                tentative_gscore = gscore[current[0]][current[1]] + 10
                if neib not in open:
                    open.append(neib)
                elif neib in open and tentative_gscore >= gscore[neib[0]][neib[1]]:
                    continue
                camefrom[neib[0]][neib[1]] = current
                gscore[neib[0]][neib[1]] = tentative_gscore
                fscore[neib[0]][neib[1]] = gscore[neib[0]][neib[1]] + misc.dist_between(neib, endpos)
    def reconstruct(self, camefrom, current):
        path = [current]
        while current != [0, 0]:
            current = camefrom[int(current[0])][int(current[1])]
            current = [int(current[0]), int(current[1])]
            path.append(current)
        return path

