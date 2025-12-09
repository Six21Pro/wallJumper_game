import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wall Jumper")

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255,255,255)

# Snake settings
snake_block = 10
snake_speed = 15

clock = pygame.time.Clock()

font = pygame.font.SysFont("comicsansms", 35)


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(win, green, [x[0], x[1], 20, snake_block])

def draw_jumper(jumper_x):

    pygame.draw.rect(win, green, [jumper_x,300,30,30])
#                  #window,color,x-pos,y-pos,width,length

def draw_wall(xpos,width,length):
    pygame.draw.rect(win,red,[xpos,0,width,length])

def draw_spike(spike_list):
    for y in spike_list:
        pygame.draw.rect(win,white,[180,y,10,5])


def message(msg, color):
    text = font.render(msg, True, color)
    win.blit(text, [width / 6, height / 3])


def game_loop():
    game_over = False
    game_close = False

    jumper_x = 180
    jumper_y = 50
    jumper_speed = 10
    jumper_move = True #initially moving to the right
    jumper_stay = True


    x = 10
    y = 10
    dx = 0
    dy = 0

    spike_y = 0

    snake_list = []
    spike_list = []
    length = 10

    food_x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            win.fill(black)
            message("Game Over! Press Q to Quit or C to Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
	    
            dy = snake_block
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0
                elif event.key == pygame.K_SPACE and jumper_stay is True:
                    #jumper_move = True
                    jumper_stay = False


           # if event.key == pygame.K_SPACE and jumper_stay is True:
                    #jumper_move = True
        if jumper_move is True and jumper_stay is False:
           jumper_x +=20 #first number was 10 which is okay
        if jumper_move is False and jumper_stay is False:
           jumper_x -=20 #DEPENDING ON THIS NUMBER I MAY NEED TO CHANGE THE BELOW STOP POINT 
        if jumper_x >= 400:
                jumper_move = False
                jumper_stay = True
        if jumper_x <= 180:
                jumper_move = True
                jumper_stay = True
	

        x += dx
        y += dy

        #if x >= width or x < 0 or y >= height or y < 0:
            #game_close = True

        win.fill(black)
        pygame.draw.rect(win, red, [food_x, food_y, snake_block, snake_block])
        


        spike_y += 10
        next_spike = []
        #next_spike.append(spike_x)
        next_spike.append(spike_y)
        
        



        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > length:
            del snake_list[0]

        #for segment in snake_list[:-1]:
            #if segment == snake_head:
                #game_close = True

        draw_snake(snake_block, snake_list)
        draw_wall(160,20,400)
        draw_wall(430,20,400)
        draw_jumper(jumper_x)
        draw_spike(next_spike)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(
                random.randrange(0, width - snake_block) / 10.0) * 10.0
            food_y = round(
                random.randrange(0, height - snake_block) / 10.0) * 10.0
            length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


game_loop()
