import pygame
import os

pygame.init()

screen = pygame.display.set_mode((640, 400))

pygame.font.init()  # you have to call this at the start,
myfont = pygame.font.SysFont("Comic Sans MS", 30)

clock = pygame.time.Clock()

running = True

while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False

    screen.fill((255, 255, 255))  # fill the screen with white

    textsurface = myfont.render('Sometext', False, (255, 0, 0))

    screen.blit(textsurface, (0, 0))

    pygame.display.update()  # update the screen

    clock.tick(40)
