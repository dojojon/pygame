#! /usr/bin/env python
import pygame
import os

pygame.init()

# try changing the file name
background = pygame.image.load("street.jpg")

screen = pygame.display.set_mode((640, 400))

clock = pygame.time.Clock()

running = True

while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False

    screen.blit(background, (0, 0))

    pygame.display.update()  # update the screen

    clock.tick(40)
