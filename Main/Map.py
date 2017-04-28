import numpy as np
import pygame
import misc

# Main Map object
# surface - This is the only required parameter and it is the surface on which you wish to draw the map (more to come with this feature
# size - The width and height of the map in cells. Format = [width, height]. Default = [10, 10]
# walls - You can pass a wall list and this will create walls in the map. Format = [[x, y], [x, y]]. Default = []
class Map():
    def __init__(self, surface, size = [10, 10], walls = []):
        self.surface = surface
        self.surfsize = surface.get_size()
        self.cellsize = [self.surfsize[0] / size[0], self.surfsize[1] / size[1]]
        self.size = size
        self.walls = np.zeros(size)
        for wall in walls:
            self.walls[wall[0]][wall[1]] = 1

    # Function to return the neighbours from a position in the map
    # currentpos - This is the loction you currently want to get the neighbours for. Format = [x, y]
    # Returns neighbours position and only returns the neighbours that are in the map and are not walls. Format = [[x, y]]
    def getneibs(self, currentpos):
        neibsUnchecked = [[currentpos[0] - 1, currentpos[1]],
                 [currentpos[0], currentpos[1] - 1],
                 [currentpos[0] + 1, currentpos[1]],
                 [currentpos[0], currentpos[1] + 1]]
        neibsChecked = []
        for neib in neibsUnchecked:
            if -1 < neib[0] < self.size[0] and -1 < neib[1] < self.size[1]:
                    if int(self.walls[neib[0]][neib[1]]) == 0:
                        neibsChecked.append(neib)
        return neibsChecked

    # This function uses the A star algorithm to solve for the shortest route through the map to a end position
    # startpos - The position you want the path to start from. Format = (x, y). Default = (0, 0)
    # endpos - The position you want to end at. Format = (x, y). Default = (). Left at default it will select bottom right corner
    # Returns the solution as a path where the 0th term is the first term and -1th is the last. Format = [[x, y], [x, y]]
    # Returns False if there is no path
    def Astar(self, startpos = (0, 0), endpos = ()):
        if not len(endpos): endpos = tuple(np.array(self.size) - 1)
        fscore, gscore, camefrom = {}, {}, {}
        gscore[startpos] = 0
        open, closed = [startpos], []
        while len(open):
            current = sorted([[fscore.get(cell, 1000**5), cell] for cell in open])[0][1]
            if current == endpos:
                return self.reconstruct(current, camefrom, startpos)

            open.pop(open.index(current))
            closed.append(current)

            for neib in self.getneibs(current):
                neib = tuple(neib)
                if neib in closed: continue

                tentative_gscore = gscore.get(current) + 10
                if neib not in open: open.append(neib)
                elif neib in open and tentative_gscore >= gscore.get(neib): continue
                camefrom[neib] = current
                gscore[neib] = tentative_gscore
                fscore[neib] = tentative_gscore + misc.dist_between(neib, endpos)
        return False

    # This function reconstructs the A star calculated path from a dictionary
    # current - The current position that you are looking at in the A star search algorithm. Format = [x, y]
    # camefrom - The dictionary of where each cell camefrom, allowing to point backwards to the original starting point. Format = {(1, 1): (0, 1)}
    # startpos - The starting position of the path. Format = [x, y]. Default = [0, 0]
    def reconstruct(self, current, camefrom, startpos = [0, 0]):
        path = [current]
        while current != startpos:
            current = camefrom.get(current)
            path.insert(0, current)
        return path

    # This function draws the map and the walls
    def draw(self):
        self.surface.fill([255, 255, 255])
        for x in range(self.size[0]):
            for y in range(self.size[1]):
                if self.walls[x][y]:
                    pygame.draw.rect(self.surface, [0, 0, 0], [self.cellsize[0] * x,
                                                               self.cellsize[1] * y,
                                                               self.cellsize[0],
                                                               self.cellsize[1]])

