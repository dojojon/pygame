# Week 4 - Count Down, Game Over and Boost Pills

## Count Down and Game Over

### Add a timer and game over boolean, just below score = 0

is_game_over = False 
time_remaining = 10
pygame.time.set_timer(pygame.USEREVENT + 1, 1000)

### Add the following to the pygame event processing
        elif event.type == pygame.USEREVENT + 1:
            print("Tick", time_remaining)

            if not is_game_over:
                time_remaining = time_remaining - 1
                if time_remaining == 0:
                    is_game_over = True

### Display the time remaining near draw score

    # Draw time
    timeText = "Time: " + str(time_remaining)
    textsurface = myfont.render(timeText, True, (0, 255, 255))
    screen.blit(textsurface, (5, 25))

###  Add the following to display game over 

    if is_game_over:
        # draw game over on screen
        game_over_surface = myfont.render("Game Over", True, (255, 0, 0))
        screen.blit(game_over_surface, (250, 160))

###  Move the player and pills into an else with tthe is_game_over

    else:
        # draw the player and the pills if we are playing
        player.update()
        player.draw(screen)  # draw the player to the screen

        pillsGroup.update()
        pillsGroup.draw(screen)

## Boost Pill - If we get time

###  Add a variable containing the image path at the top
boost_img_path = 'boost.png'


### Add  to the Pill Class so we can have a special pill

is_boost = False

### add boost to the constructor of pill class

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

### Update the create pills to create score and boost pills

for num in range(0, 15):
    pill = Pill(False)  # Create a score pill

for num in range(0, 2):
    pill = Pill(True)  # Create a boots pill


###  Update the kill function to add the time remaining if a boost pill

        global time_remaining
        if self.is_boost:
            time_remaining = time_remaining + 1
