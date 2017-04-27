import Map
import misc
import time
import numpy as np


class AI():
    def __init__(self, Map, roi = [7, 7, 10, 10], startpos = [0, 0], speed = 100, sspeed = 100):
        self.map = Map
        self.roi = roi
        self.currentpos = startpos
        self.speed = speed
        self.sprintspeed = sspeed
        self.currentpath = []
        self.frame = 0
        self.lastmove = 0


    def wander(self):
        print(time.time() > 5000)
        if not len(self.currentpath) and time.time() - self.lastmove > 5000:
            x, y = np.random.randint(self.roi[0], self.roi[2]), np.random.randint(self.roi[1], self.roi[3])
            self.moveto([19, 19])
            self.lastmove = time.time()

    def moveto(self, pos):
        path = self.map.Astar(self.currentpos, pos)
        self.currentpath = path[:-1]

    def move(self):
        self.frame += 1
        if self.frame % self.speed == 0:
            if len(self.currentpath):
                self.currentpos = self.currentpath.pop(-1)
        if not len(self.currentpath):
            self.wander()
