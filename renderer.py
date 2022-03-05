from math import cos, sin

import pygame
from pygame import Rect, Vector2, Vector3

from settings import *

# class Vector2:
#     def __init__(self, x, y):
#         if not isinstance(x, int):
#             self.x = vector
class Camera:
    def __init__(self, pos=(50, 50, -200)):
        self.pos = Vector3(pos)
        self.orientation = Vector3(0, 0, 0)
        self.FOV = 200
        self.sensitivity = 0.1
        self.speed = 1

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                y, x = event.rel
                self.orientation += (x/self.FOV*self.sensitivity, y/self.FOV*self.sensitivity, 0)
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.pos.z += dt*self.speed
        if keys[pygame.K_s]:
            self.pos.z -= dt*self.speed
        if keys[pygame.K_d]:
            self.pos.x += dt*self.speed
        if keys[pygame.K_a]:
            self.pos.x -= dt*self.speed

class Mesh:
    def __init__(self, points = [], faces=[]):
        self.vertices = [Vector3(p) for p in points]
        self.faces = faces

    def scale(self, scale=1):
        self.points = [Vector3(p.x*scale, p.y*scale, p.z*scale) for p in self.vertices]
    
class Scene:
    def __init__(self, c, objs=[], scale=-100):
        self.view = Vector3(winWidth/2, winHeight/2, 1)
        self.camera = c
        self.scale = scale
        self.objects = objs
        for o in objs:
            o.scale(self.scale)
        
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
        f = self.camera.FOV

        b.x = ((e.z+f)/(d.z+f))*d.x + e.x
        b.y = ((e.z+f)/(d.z+f))*d.y + e.y

        return b

    def inView(self, vec):
        if vec.x > winWidth or vec.y > winHeight or vec.x < 0 or vec.y < 0:
            return False
        return True
    
    def render(self, win):
        for o in self.objects:
            # for v in o.vertices:
            #     p = self.project(self.transform(v))
            #     pygame.draw.circle(win, green, p, 1)

            for f in o.faces:
                pygame.draw.polygon(win, green, [self.project(self.transform(o.points[p])) for p in f], 1)

    def update(self):
        self.camera.update()