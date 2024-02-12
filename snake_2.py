import pygame
import time
pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake gmae - by Yang")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# Fonts for the game 
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)

quit_game = False

# setting up the size of the snake
# X value is 490, as the size of the  window horizontally is 1000,
# and takeaway snake's width (20px), therefore (1000-20)/2 = 490
snake_x = 490 

# Since size is 1000x750, the snake's height is also 20px.
# therefore (750-20)/2 = 365
snake_y = 365

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
    
    # pygame.draw.rect() function draws a rectangle on the screen.
    # Inside bracket, it must include in following order:
    # Surface on which the rectangle is to be drawn, e.g screen
    # the colour  of the rectangle
    # x, and y coordinates for the rectangle
    # the width and height of the rectangle
    pygame.draw.rect(screen, red, [snake_x, snake_y, 20, 20])

    # pygame.display.update() fuction updates the surface
    # to show the changes the program just made.
    pygame.display.update()

pygame.quit()
quit()