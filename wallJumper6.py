#This  IS REALLY JUST wallJumper4 but CLEANED UP
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
yellow = (255,255,0)


clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 25)


def draw_jumper(jumper_x):

    pygame.draw.rect(win, green, [jumper_x,300,30,30])
#                  #window,color,x-pos,y-pos,width,length

def draw_wall(xpos,width,length):
    pygame.draw.rect(win,red,[xpos,0,width,length])


def draw_spike2(sp_y):
    for y in sp_y:
        pygame.draw.rect(win,white,[180,y,10,5])

def draw_spike3(sp_y):
    for y in sp_y:
        pygame.draw.rect(win,white,[420,y,10,5])

def draw_coin(coin_list):
    for c in coin_list:
        pygame.draw.rect(win,yellow,[410,c,5,5])

def draw_coin2(coin_list):
    for c in coin_list:
        pygame.draw.rect(win,yellow,[190,c,5,5])

def draw_heart():
    pygame.draw.rect(win, red,[490,150,5,5])
    pygame.draw.rect(win, red,[497,150,5,5])
    pygame.draw.rect(win, red,[492,152,8,5])
    pygame.draw.rect(win, red,[494,154.5,4,5])
    pygame.draw.rect(win, red,[491,148,3,2])
    pygame.draw.rect(win, red,[498,148,3,2])
   # pygame.draw.rect(win, red,[489,151,2,2])
    #pygame.draw.rect(win, red,[501,151,2,2])


def message(msg, color,x,y):
    text = font.render(msg, True, color)
    win.blit(text, [x, y])


def game_loop():
    game_over = False
    game_close = False

    jumper_x = 180
    jumper_move = True #initially moving to the right
    jumper_stay = True

    x = 10
    y = 10
    spike_y = 0
    coin_count = 0
    lives_count = 0

    length = 10
    spy = []
    spy2 = []
    coin_list1 = []
    coin_list2 = []


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
	          
        
            if event.type == pygame.KEYDOWN:                              
                if event.key == pygame.K_SPACE and jumper_stay is True:
                    #jumper_move = True
                    jumper_stay = False

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
	

        win.fill(black)  


        spike_y += 10


        randy = random.randint(1, 40)  # e.g., 7
        if randy == 6:
           spy.append(0)
        if randy == 11:
           spy2.append(0)
        if randy == 5:
           coin_list1.append(0)
        if randy == 3:
           coin_list2.append(0)

        draw_coin2(coin_list1)
        draw_coin(coin_list2)
        draw_spike2(spy)
        draw_spike3(spy2)

        for i in range(len(spy)):
           spy[i] = spy[i] + 10

        for i in range(len(spy)):
           if jumper_x <= 190 and spy[i] == 300:
              print("loss")

        for i in range(len(spy2)):
           spy2[i] = spy2[i] + 10

        for i in range(len(spy2)):
           if jumper_x >= 380 and spy2[i] == 300:
              print("loss")



        for i in range(len(coin_list1)):
           coin_list1[i] = coin_list1[i] + 5

        for i in range(len(coin_list2)):
           coin_list2[i] = coin_list2[i] + 5

        for i in range(len(coin_list2)):
           if jumper_x >= 380 and coin_list2[i] == 300:
              print("coin")
              coin_count += 1

        for i in range(len(coin_list1)):
           if jumper_x <= 180 and coin_list1[i] == 300: 
              print("coin")
              coin_count += 1

        jumper_rect = pygame.Rect(jumper_x, 300, 30, 30).inflate(5,5)
        for y in coin_list2:
            coin_rect = pygame.Rect(410, y, 5, 5)

            pygame.draw.rect(win, (255, 0, 255), coin_rect, 1)  # Magenta coin box

            if jumper_rect.colliderect(coin_rect):

               print("coin")
               coin_list2.remove(y)
               coin_count += 1
               break



        for y in coin_list1:
            coin_rect = pygame.Rect(190, y, 5, 5)

            pygame.draw.rect(win, (255, 0, 255), coin_rect, 1)  # Magenta coin box

            if jumper_rect.colliderect(coin_rect):

               print("coin")
               coin_list1.remove(y)
               coin_count += 1
               break

        pygame.draw.rect(win, (0, 0, 255), jumper_rect, 2)  # Blue jumper box



        if coin_count == 15:
           coin_count = 0
           lives_count += 1

        
        spy = [y for y in spy if y < height]
        spy2 = [y for y in spy2 if y < height]

        coin_list1 = [y for y in coin_list1 if y < height]
        coin_list2 = [y for y in coin_list2 if y < height]

 
        draw_wall(160,20,400)
        draw_wall(430,20,400)
        money = str(coin_count)
        hearts = str(lives_count)
        message("COIN$: "+money, yellow,10,10)
        message("LIVES: "+hearts,red,470,10)

        draw_heart()



        draw_jumper(jumper_x)

        pygame.display.update()

        clock.tick(15)

    pygame.quit()
    quit()


game_loop()
