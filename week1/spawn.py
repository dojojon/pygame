import pygame
import os
import random

# it is better to have an extra variable, than an extremely long line.
player_img_path = 'player.png'
pill_img_path = 'pill.png'


class Pill(object):

    def __init__(self):
        self.image = pygame.image.load(pill_img_path)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 100
        self.alive = True

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        print("Pill", self.rect)
        if self.alive:
            surface.blit(self.image, (self.rect.x, self.rect.y))

    def is_collided_with(self, player):
        return self.rect.colliderect(player.rect)

    def eat(self):
        self.rect.x = random.randrange(100, 540)
        self.rect.y = random.randrange(100, 300)


class Player(object):  # represents the player, not the game

    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load(player_img_path)
        # collision rectangle
        self.rect = self.image.get_rect()

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        dist = 1  # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]:  # down key
            self.rect.y += dist  # move down
        elif key[pygame.K_UP]:  # up key
            self.rect.y -= dist  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.rect.x += dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.rect.x -= dist  # move left

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.rect.x, self.rect.y))
        print(self.rect)

pygame.init()

screen = pygame.display.set_mode((640, 400))

pill = Pill()  # Create a pill
player = Player()  # create an instance of player
clock = pygame.time.Clock()

running = True

while running:

    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False

    player.handle_keys()  # handle the keys

    if pill.is_collided_with(player):
        pill.eat()

    screen.fill((255, 255, 255))  # fill the screen with white
    player.draw(screen)  # draw the player to the screen
    pill.draw(screen)

    pygame.display.update()  # update the screen

    clock.tick(40)  # Limit the game to running at 40 frames per second
