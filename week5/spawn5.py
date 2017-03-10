#! /usr/bin/env python
# import os
import pygame
import random

# it is better to have an extra variable, than an extremely long line.
player_img_path = 'player.png'
pill_img_path = 'pill.png'
boost_img_path = 'boost.png'

background = pygame.image.load("space.jpg")

# create a group for all the pills
pillsGroup = pygame.sprite.Group()


class Pill(pygame.sprite.Sprite):

    is_boost = False

    def __init__(self, boost):
        pygame.sprite.Sprite.__init__(self, pillsGroup)
        self.is_boost = boost
        if self.is_boost:
            self.image = pygame.image.load(boost_img_path)
        else:
            self.image = pygame.image.load(pill_img_path)
        self.rect = self.image.get_rect()
        self.warp()
        self.alive = True

    def draw(self, surface):
        global myfont
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.rect.x, self.rect.y))

    def kill(self):
        global time_remaining
        """ When eaten, warp """
        if self.is_boost:
            time_remaining = time_remaining + 1
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
        dist = 4  # distance moved in 1 frame, try changing it
        if key[pygame.K_DOWN]:  # down key
            self.rect.y += dist  # move down
        elif key[pygame.K_UP]:  # up key
            self.rect.y -= dist  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.rect.x += dist  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.rect.x -= dist  # move left

    def update(self):
        global score
        """ Update the player """
        player.handle_keys()  # handle the keys

        if pygame.sprite.spritecollide(self, pillsGroup, True):
            score = score + 1
            print ("Player ate Pill Score", score)

    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.image, (self.rect.x, self.rect.y))

pygame.init()

clock = pygame.time.Clock()

score = 0
is_game_over = False
time_remaining = 10
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

pygame.font.init()
myfont = pygame.font.SysFont("Serif", 30)

screen = pygame.display.set_mode((640, 400))

# Create pills
for num in range(0, 15):
    pill = Pill(False)  # Create a pill

for num in range(0, 2):
    pill = Pill(True)  # Create a pill

player = Player()  # create an instance of player

running = True

while running:

    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()  # quit the screen
            running = False
        elif event.type == pygame.USEREVENT + 1:
            print("Tick", time_remaining)

            if not is_game_over:
                time_remaining = time_remaining - 1
                if time_remaining == 0:
                    is_game_over = True

    screen.fill((255, 255, 255))  # fill the screen with white

    screen.blit(background, (0, 0))

    # Draw score
    scoreText = "Score: " + str(score)
    textsurface = myfont.render(scoreText, True, (255, 255, 255))
    screen.blit(textsurface, (5, 5))

    # Draw time
    timeText = "Time: " + str(time_remaining)
    textsurface = myfont.render(timeText, True, (0, 255, 255))
    screen.blit(textsurface, (5, 25))

    if is_game_over:
        game_over_surface = myfont.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_surface, (250, 160))
    else:
        player.update()
        player.draw(screen)  # draw the player to the screen

        pillsGroup.update()
        pillsGroup.draw(screen)

    pygame.display.update()  # update the screen

    clock.tick(40)  # Limit the game to running at 40 frames per second
