import pygame
from settings import *
from pygame import Vector2, Vector3
from renderer import Camera, Scene, Mesh

import pickle

pygame.init()

pygame.event.get()
pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygame.event.set_grab(True)

win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("3d POWER")

# Cube
points = [(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1)]
load = pickle.load( open( "out.p", "rb" ) )
heart = Mesh(points, [(0,1,2,3), (4,5,6,7), (0,1,5,4), (2,3,7,6), (1,2,6,5), (0,3,7,4)]) #Mesh(load['v'], load['f'])
cam = Camera()
s = Scene(cam, [heart])

while True:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEMOTION:
            y, x = event.rel; x /= s.FOV; y /= s.FOV; cam.orientation.x += x; cam.orientation.y += y
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        cam.pos.z += 1
    if keys[pygame.K_DOWN]:
        cam.pos.z -= 1
    if keys[pygame.K_RIGHT]:
        cam.pos.x += 1
    if keys[pygame.K_LEFT]:
        cam.pos.x -= 1

    win.fill(black)
    s.render(win)
    # cam.orientation.y += 0.01
    pygame.display.update()

pygame.quit()