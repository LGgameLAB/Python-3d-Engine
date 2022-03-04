from math import cos, sin

import pygame
from pygame import Vector2, Vector3

from settings import *

class Camera:
    def __init__(self, pos=(0.8, -2.3, -200)):
        self.pos = Vector3(pos)
        self.orientation = Vector3(-0.7, 0, 0)

class Scene:
    def __init__(self, c, objs=[], scale=100):
        self.view = pygame.Vector3(winWidth/2, winHeight/2, 1)
        self.camera = c
        self.scale = scale
        self.FOV = 1000
        self.objects = [pygame.Vector3(o[0]*scale, o[1]*scale, o[2]*scale) for o in objs]
    
    def transform(self, vec):
        '''
        Transforms a 3d vector
        '''
        d = Vector3(0, 0, 0)
        a = pygame.Vector3(vec)

        c = self.camera.pos
        o = self.camera.orientation

        X = a.x-c.x
        Y = a.y-c.y
        Z = a.z-c.z

        sx = sin(o.x)
        sy = sin(o.y)
        sz = sin(o.z)
        cx = cos(o.x)
        cy = cos(o.y)
        cz = cos(o.z)

        d.x = cy*(sz*Y + cz*X) - sy*Z
        d.y = sx*(cy*Z + sy*(sz*Y + cz*X)) + cx*(cz*Y - sz*X)
        d.z = cx*(cy*Z + sy*(sz*Y + cz*X)) - sx*(cz*Y - sz*X)

        return d

    def project(self, vec):
        '''
        Projects a 3d vector onto 2d space
        '''
        b = Vector2(0, 0)
        d = vec

        e = self.view
        f = self.FOV

        b.x = ((e.z+f)/(d.z+f))*d.x + e.x
        b.y = ((e.z+f)/(d.z+f))*d.y + e.y

        return b
    
    def render(self, win):
        for o in self.objects:
            pygame.draw.circle(win, green, self.project(self.transform(o)), 1)
