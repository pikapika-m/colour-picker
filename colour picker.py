import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 240),pygame.RESIZABLE)

pygame.display.set_caption('Press r/g/b to change colour')

running = True
r,g,b = 0,0,0
background = [r,g,b]
brightness=[0,64,128,192,255]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                r=(r+1)%3
            elif event.key == pygame.K_g:
                g=(g+1)%3
            elif event.key == pygame.K_b:
                b=(b+1)%3
            background=brightness[r],brightness[g],brightness[b]

    screen.fill(background)
    pygame.display.update()

pygame.quit()