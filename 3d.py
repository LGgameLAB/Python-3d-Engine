import pygame
from settings import *
from pygame import Vector2, Vector3
from renderer import Camera, Scene

pygame.init()


win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption("3d POWER")

# Cube
points = [(1, 1, 1), (-1, 1, 1), (-1, -1, 1), (1, -1, 1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1), (1, -1, -1)]
cam = Camera()
s = Scene(cam, points)

while True:
    pygame.time.delay(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        cam.pos.z += 1

    win.fill(black)
    s.render(win)
    cam.orientation.x += 0.01
    pygame.display.update()



pygame.quit()                      

