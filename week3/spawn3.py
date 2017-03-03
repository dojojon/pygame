#! /usr/bin/env python
#import os
import pygame
import random

# it is better to have an extra variable, than an extremely long line.
player_img_path = 'player.png'
pill_img_path = 'pill.png'

# create a group for all the pills
pillsGroup = pygame.sprite.Group()


class Pill(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, pillsGroup)
        self.image = pygame.image.load(pill_img_path)
        self.rect = self.image.get_rect()
        self.warp()
        self.alive = True

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def kill(self):
        """ When eaten, warp """
        print ("Pill eaten")
        self.warp()

    def warp(self):
        """ Random position of pill """
        self.rect.x = random.randrange(100, 540)
        self.rect.y = random.randrange(100, 300)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(player_img_path)
        self.rect = self.image.get_rect()

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 2  # distance moved in 1 frame, try changing it
        if key[pygame.K_DOWN]:  # down key
            self.rect.y += dist  # move down
        elif key[pygame.K_UP]:  # up key
            self.rect.y -= dist  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.rect.x += dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.rect.x -= dist  # move left

    def update(self):
        """ Update the player """
        player.handle_keys()  # handle the keys

        if pygame.sprite.spritecollide(self, pillsGroup, True):
            print ("Player ate Pill")

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.rect.x, self.rect.y))

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((640, 400))

# Create pills
for num in range(0, 5):
    pill = Pill()  # Create a pill

player = Player()  # create an instance of player

running = True

while running:

    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False

    screen.fill((255, 255, 255))  # fill the screen with white

    player.update()
    player.draw(screen)  # draw the player to the screen

    pillsGroup.update()
    pillsGroup.draw(screen)

    pygame.display.update()  # update the screen

    clock.tick(40)  # Limit the game to running at 40 frames per second
