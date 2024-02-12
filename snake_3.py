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

clock = pygame.time.Clock() # sets the speed at which the snake moves

quit_game = False

# setting up the size of the snake
# X value is 490, as the size of the  window horizontally is 1000,
# and takeaway snake's width (20px), therefore (1000-20)/2 = 490
snake_x = 490 

# Since size is 1000x750, the snake's height is also 20px.
# therefore (750-20)/2 = 365
snake_y = 365

snake_x_change = 0 # holds the value of changes in the x coordinate of the snake
snake_y_change = 0 # holds the value of changes in the y coordinate of the snake

while not quit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game = True
        
        # instructs the snake to move in the x and y direction by 20 pixels
        # as up, down, right, and left keys are pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -20
                snake_y_change = 0
            if event.key == pygame.K_RIGHT:
                snake_x_change = 20
                snake_y_change  = 0
            if event.key == pygame.K_UP:
                snake_y_change = -20
                snake_x_change = 0
            if event.key == pygame.K_DOWN:
                snake_y_change = 20
                snake_x_change = 0

    # If snake is out of boundaries(edge of the window), then the  game finishes
    if snake_x >= 1000 or snake_x <= 0 or snake_y >= 720 or snake_y <= 0:
        quit_game = True

    # changes the x and y coordinates of the snake

    snake_x += snake_x_change
    snake_y += snake_y_change

    screen.fill(green) # changes screen from default black to green


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

    clock.tick(5) # sets the speed at which each iteration of  the game loop
    # runs in frames per second (fps), In this case it is set to 5 fps.

pygame.quit()
quit() 