#! /usr/bin/env python
import pygame
import os

pygame.init()

screen = pygame.display.set_mode((640, 400))

pygame.font.init()  # you have to call this at the start,
# try changing the size, Roboto
myfont = pygame.font.SysFont("Comic Sans MS", 30)

clock = pygame.time.Clock()

running = True

while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False

    # fill the screen with white,  try changing the color
    screen.fill((255, 255, 255))

    # try chaning the Hello dojo, try changing the color, try changing False
    # to True
    textsurface = myfont.render('Hello DoJo', False, (255, 0, 0))

    print("texture rect", textsurface.get_rect())
    screen.blit(textsurface, (0, 0))

    pygame.display.update()  # update the screen

    clock.tick(40)
