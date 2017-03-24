# Week 5 Highscores and Play Again

## High scores

Open up highscores and review the code

Run it

### Add is_high_score_and_save function and test

def is_high_score_and_save(score):

    # Get the current high score
    high_score = get_high_score()

    # set variable to true if high score
    is_high_score = score > high_score

    # Only save score if its a high score
    if is_high_score:
        save_high_score(score)

    # return the result
    return is_high_score

### Import high scores function into spawn and integrate

At top of spawn6.py add the following to import the function

from highscore import is_high_score_and_save

###  Add variable to track high score state

Near is_game_over add

is_high_score = False

## Call the is_high_score_and_save function call 

Find where we set is_game_over = True and add the following

is_high_score = is_high_score_and_save(score)

### Display new high score message on game over

In the game over state add the following.

if is_high_score:
    high_score_text = "High Score " + str(score)
    high_score_surface = myfont.render(
        high_score_text, True, (255, 255, 0))
    screen.blit(high_score_surface, (250, 350))

## Play Again

### Add a message to tell the player what to do

press_to_play_surface = myfont.render("Press Space to Play Again", True, (255, 255, 255))
screen.blit(press_to_play_surface, (200, 370))

### Add code for a key pressed to space
key = pygame.key.get_pressed()
if key[pygame.K_SPACE]:  
    score = 0
    is_game_over = False
    is_high_score = False
    time_remaining = 10
    
### Add this code to randomise the pill start positions
    for pill in pillsGroup:
        pill.warp()

