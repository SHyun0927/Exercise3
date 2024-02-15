import pygame
import time
import random
pygame.init()

screen = pygame.display.set_mode((1000, 750))
game_icon = pygame.image.load('snake_icon.png')
pygame.display.set_icon(game_icon)
pygame.display.set_caption("Snake gmae - by Yang")

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)

# Fonts for the game 
score_font = pygame.font.SysFont("arialblack", 20)
exit_font = pygame.font.Font("freesansbold.ttf", 30)
msg_font = pygame.font.SysFont("arialblack", 20)

# Stpes we must follow in order to display messages through pygame
# 1. Create font object - using font.Font() or font.SysFont().
# 2. Create text surface object - using render() method.
# 3. Create rectangle object for text surface object - using get_rect() method.
# 4. Copy the 'Text' surface object to your 'Display' surface object - using  blit method.
# 5. Update the Display surface object - using display.update() method.
def message(msg, text_colour, bkgd_colour):
    # render() method  is applied to the font object (message). 
    # The arguments are:
    # message to be displayed,
    # Antialiasing (True/False)
    # Font colour
    # Background colour (optional, default transparent.)
    txt = msg_font.render(msg, True, text_colour, bkgd_colour)

    # Centre rectangle = 1000/2 = 500, 720/2 = 360
    text_box = txt.get_rect(center=(500, 360))

    # blit() method is used frequrently, it draws one image on another.
    # The arugements are:
    # source - image to be drawn
    # destination - image on which it is drawn
    # If no text_box, you can give coordinates. (e.g. (400, 360) )
    screen.blit(txt, text_box)



clock = pygame.time.Clock() # sets the speed at which the snake moves

quit_game = False

# setting up the size of the snake
# X value is 490, as the size of the  window horizontally is 1000,
# and takeaway snake's width (20px), therefore (1000-20)/2 = 490
snake_x = 490 

# Since size is 1000x750, the snake's height is also 20px.
# therefore (720-20)/2 = 360
snake_y = 370

snake_x_change = 0 # holds the value of changes in the x coordinate of the snake
snake_y_change = 0 # holds the value of changes in the y coordinate of the snake

# setting a random position for the food at the start. 
food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
food_y = round(random.randrange(20, 720 - 20) / 20) * 20


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

    # creating food
    pygame.draw.circle(screen, yellow, [food_x, food_y], 10)
    pygame.display.update() 
    
    # collision detection (for food)
    if snake_x == food_x +- 10 and snake_y == food_y +- 10:
        food_x = round(random.randrange(20, 1000 - 20) / 20) * 20
        food_y = round(random.randrange(20, 720 - 20) / 20) * 20


    clock.tick(5) # sets the speed at which each iteration of  the game loop
    # runs in frames per second (fps), In this case it is set to 5 fps.

# updating the message 'You Died!' to screen
# black font, white background colour
message("You Died!", black, white)
pygame.display.update()
time.sleep(3)


pygame.quit()
quit() 