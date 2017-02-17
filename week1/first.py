import pygame
import os

pygame.init()

screen = pygame.display.set_mode((640, 400))

clock = pygame.time.Clock()

running = True

while running:

    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False

    screen.fill((255, 100, 255))  # fill the screen with white

    pygame.display.update()  # update the screen

    clock.tick(40)  # Limit the game to running at 40 frames per second
