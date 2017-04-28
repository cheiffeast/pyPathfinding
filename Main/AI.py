import time
import pygame
import numpy as np


class AI():
    def __init__(self, Map, roi = [7, 7, 15, 15], startpos = [0, 0], speed = 10, sspeed = 100):
        self.map = Map
        self.roi = roi
        self.currentpos = startpos
        self.speed = speed
        self.sprintspeed = sspeed
        self.currentpath = []
        self.frame = 0
        self.lastmove = 0


    def wander(self):
        if time.time() - self.lastmove > 3 + (np.random.randint(0, 3000) / 1000):
            x, y = np.random.randint(self.roi[0], self.roi[2]), np.random.randint(self.roi[1], self.roi[3])
            self.moveto([x, y])
            self.lastmove = time.time()

    def moveto(self, pos):
        path = self.map.Astar(tuple(self.currentpos), tuple(pos))
        self.currentpath = path[1:]

    def move(self):
        self.frame += 1
        if self.frame % self.speed == 0:
            if len(self.currentpath):
                self.currentpos = self.currentpath.pop(0)
        if not len(self.currentpath):
            self.wander()
