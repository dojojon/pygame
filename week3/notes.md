# Week 3 - Backgrounds, Text and Scores recap

## Add background

 * This line loads in image into background (surface)
background = pygame.image.load("street.jpg")

* This line draws the background
screen.blit(background, (0, 0))

## Display text

* You have to call this at the start,

pygame.font.init()  

* Set up a font, try changing the size, Roboto

myfont = pygame.font.SysFont("Comic Sans MS", 30)

* Draw the text to a surface
* Try changing the 'Hello Dojo;
* Try changing the color
* Try changing False to True, anti aliasing
* Try changing the position (0,0)  x , y
textsurface = myfont.render('Hello DoJo', False, (255, 0, 0))

* blit the surface to the screen
screen.blit(textsurface, (0, 0))

## Score

* Add a global variable called score and set to zero
score = 0

* Find the code that get run when a player eats a pill
* Add to score
score = score + 1

* Print the score out
print ("Score", score)

* Does it update?
* We need to make the global variable available to the function

global score

* Change the text to print the score out
scoreText = "Score " + str(score)
textsurface = myfont.render(scoreText, False, (255, 0, 0))

## Draw text centered (Extended)

* get the text surface width

textRect = textsurface.get_rect()
textWidth = textRect.width

* subtract it from screen width and divide by 2
textX = (640 - textWidth) / 2

screen.blit(textsurface, (textX, 0))