
import pygame
import time
import random

# Initialize pygame
pygame.init()

# Set up display
width, height = 600, 400
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Wall Jumper")#game name

# Colors
black = (0, 0, 0)
green = (0, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)


clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsansms", 25)


def draw_jumper(jumper_x):

    pygame.draw.rect(win, green, [jumper_x, 300, 30, 30])


#                  #window,color,x-pos,y-pos,width,length


def draw_wall(xpos, width, length):#draw functions are all used to generate objects in the game
    pygame.draw.rect(win, red, [xpos, 0, width, length])


def draw_spike2(sp_y):#draw left spikes
    for y in sp_y:
        pygame.draw.rect(win, white, [180, y, 10, 5])


def draw_spike3(sp_y):#draw right spikes
    for y in sp_y:
        pygame.draw.rect(win, white, [420, y, 10, 5])


def draw_coin(coin_list):#draw right coins
    for c in coin_list:
        pygame.draw.rect(win, yellow, [410, c, 5, 5])


def draw_coin2(coin_list):#draw left coins #NOTICE MY NAMING SCHEME IS CONFUSING, REVERSED AND SHOULD BE HANDLED BETTER IN THE FUTURE.
    for c in coin_list:
        pygame.draw.rect(win, yellow, [190, c, 5, 5])


def draw_heart():#template. This draws outside the right wall

    pygame.draw.rect(win, red, [490, 150, 5, 5])
    pygame.draw.rect(win, red, [497, 150, 5, 5])
    pygame.draw.rect(win, red, [492, 152, 8, 5])
    pygame.draw.rect(win, red, [494, 154.5, 4, 5])
    pygame.draw.rect(win, red, [491, 148, 3, 2])
    pygame.draw.rect(win, red, [498, 148, 3, 2])
# pygame.draw.rect(win, red,[489,151,2,2])
# pygame.draw.rect(win, red,[501,151,2,2])


def draw_heart2(h_list):#draw left hearts
    for y in h_list:
        pygame.draw.rect(win, red, [195, y, 5, 5])
        pygame.draw.rect(win, red, [202, y, 5, 5])
        pygame.draw.rect(win, red, [197, y + 2, 8, 5])
        pygame.draw.rect(win, red, [199, y + 4.5, 4, 5])
        pygame.draw.rect(win, red, [196, y - 2, 3, 2])
        pygame.draw.rect(win, red, [203, y - 2, 3, 2])
# pygame.draw.rect(win, red,[489,151,2,2])
# pygame.draw.rect(win, red,[501,151,2,2])


def draw_heart3(h_list):#draw right hearts
    for y in h_list:
        pygame.draw.rect(win, red, [400, y, 5, 5])
        pygame.draw.rect(win, red, [407, y, 5, 5])
        pygame.draw.rect(win, red, [402, y + 2, 8, 5])
        pygame.draw.rect(win, red, [404, y + 4.5, 4, 5])
        pygame.draw.rect(win, red, [401, y - 2, 3, 2])
        pygame.draw.rect(win, red, [408, y - 2, 3, 2])
# pygame.draw.rect(win, red,[489,151,2,2])
# pygame.draw.rect(win, red,[501,151,2,2])


def message(msg, color, x, y):#used to display messages
    text = font.render(msg, True, color)
    win.blit(text, [x, y])


def game_loop():
    game_over = False
    game_close = False

    jumper_x = 180
    jumper_move = True  # initially jumper is moving to the right
    jumper_stay = True

    x = 10
    y = 10
    spike_y = 0
    coin_count = 0
    lives_count = 3
    total_coins = 0

    length = 10
    spy = []#list for spikes
    spy2 = []#list for right spikes
    coin_list1 = []#list for left coins
    coin_list2 = []#list for right coins
    heart_list1 = []#list for left hearts
    heart_list2 = []#list for right hearts

    while not game_over:

        while game_close:
            win.fill(black)
            message("Game Over! Press Q to Quit or C to Play Again", red,10,10)
            message("You collected " +str(total_coins)+  " Coins!!", yellow,10,40)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:#if user wishes to exit the game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:#if user wishes to replay the game
                        game_loop()#game will begin again. Recursion.

        for event in pygame.event.get():#REDUNDANT?
            if event.type == pygame.QUIT:
                game_over = True
                
                

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and jumper_stay is True:
                    # jumper_move = True
                    jumper_stay = False

        if jumper_move is True and jumper_stay is False:#used to move the jumper right
            jumper_x += 20  # first number was 10 which is okay
        if jumper_move is False and jumper_stay is False:#used to move the jumper left
            jumper_x -= (
                20  # DEPENDING ON THIS NUMBER I MAY NEED TO CHANGE THE BELOW STOP POINT
            )
        if jumper_x >= 400:#makes the jumper stop at the right wall
            jumper_move = False
            jumper_stay = True
        if jumper_x <= 180:#makes the jumper stop at the left wall
            jumper_move = True
            jumper_stay = True

        win.fill(black)

        spike_y += 10

        randy = random.randint(1, 40)  # used to randomly generate spikes and coins
        randy2 = random.randint(1, 600) # used for randomly generating hearts, which I want to happen unfrequently
        if randy == 6:
            spy.append(0)
        if randy == 11:
            spy2.append(0)#right spike
        if randy == 5:
            coin_list1.append(0)#append a left coin
        if randy == 3:
            coin_list2.append(0)#append a right coin
        if randy2 == 5:
            heart_list1.append(0)#draw a left heart
        if randy2 == 6:
            heart_list2.append(0)

        draw_coin2(coin_list1)#draw a left coin
        draw_coin(coin_list2)#draw a right coin
        draw_spike2(spy)#draw a left spike
        draw_spike3(spy2)#draw a right spike
        draw_heart2(heart_list1)#draw a left heart
        draw_heart3(heart_list2)#draw a right heart

        for i in range(len(spy)):#moves left spikes down by 10
            spy[i] = spy[i] + 10

        for i in range(len(spy)):
            if jumper_x <= 190 and spy[i] == 300:#if a left spike hits the jumper
                print("loss")
                lives_count -= 1

        for i in range(len(spy2)):#moves right spikes down by 10
            spy2[i] = spy2[i] + 10

        for i in range(len(spy2)):
            if jumper_x >= 380 and spy2[i] == 300:#if a right spike hits the jumper
                print("loss")
                lives_count -= 1

        for i in range(len(coin_list1)):#moves left coins down by 5
            coin_list1[i] = coin_list1[i] + 5

        for i in range(len(coin_list2)):#moves coins down by 5
            coin_list2[i] = coin_list2[i] + 5

        for i in range(len(heart_list1)):#moves hearts down by 5
            heart_list1[i] = heart_list1[i] + 5

        for i in range(len(heart_list2)):#moves right hearts down by 5
            heart_list2[i] = heart_list2[i] + 5

        for i in range(len(coin_list2)):#This is responsible for removing right coins upon collision with the jumper
            for y in coin_list2[:]:
                if jumper_x >= 380 and y == 300:
                    print("coin")
                    coin_count += 1
                    total_coins += 1 
                    coin_list2.remove(y)

        for i in range(len(coin_list1)):#This is responsible for removing left coins upon collision with the jumper
            for y in coin_list1[:]:
                if jumper_x <= 180 and y == 300:
                    print("coin")
                    coin_count += 1
                    total_coins += 1
                    coin_list1.remove(y)

        for i in range(len(heart_list1)): #This is responsible for removing left hearts upon collision with the jumper
            for y in heart_list1[:]:
                if jumper_x <= 180 and heart_list1[i] == 300:
                    print("life")
                    lives_count += 1
                    heart_list1.remove(y)

        for i in range(len(heart_list2)): #This is responsible for removing right hearts upon collision with the jumper
            for y in heart_list2[:]:
                if jumper_x >= 380 and heart_list2[i] == 300:
                    print("life")
                    lives_count += 1
                    heart_list2.remove(y)

        jumper_rect = pygame.Rect(jumper_x, 300, 30, 30).inflate(5, 5)
        # for y in coin_list2:
        #     coin_rect = pygame.Rect(410, y, 5, 5)

        #     pygame.draw.rect(win, (255, 0, 255), coin_rect, 1)  # Magenta coin box

        #     if jumper_rect.colliderect(coin_rect):

        #         print("coin")
        #         coin_list2.remove(y)
        #         coin_count += 1
        #         total_coins += 1
        #         break

        # for y in coin_list1:
        #     coin_rect = pygame.Rect(190, y, 5, 5)

        #     pygame.draw.rect(win, (255, 0, 255), coin_rect, 1)  # Magenta coin box

        #     if jumper_rect.colliderect(coin_rect):

        #         print("coin")
        #         coin_list1.remove(y)
        #         coin_count += 1
        #         total_coins += 1
        #         break

        pygame.draw.rect(win, (0, 0, 255), jumper_rect, 2)  # Blue jumper box

        if coin_count == 15:#if 15 coins collected, gain a life
            coin_count = 0
            lives_count += 1

        spy = [y for y in spy if y < height]#intention is for these lists to remove entities that go beyond the desired game height
        spy2 = [y for y in spy2 if y < height]#list of right spikes

        coin_list1 = [y for y in coin_list1 if y < height]
        coin_list2 = [y for y in coin_list2 if y < height]

        heart_list1 = [y for y in heart_list1 if y < height]
        heart_list2 = [y for y in heart_list2 if y < height]

        draw_wall(160, 20, 400)
        draw_wall(430, 20, 400)
        money = str(coin_count)#convert int to a string
        hearts = str(lives_count)
        message("COIN$: " + money, yellow, 10, 10)
        message("LIVES: " + hearts, red, 470, 10)

        draw_heart()

        draw_jumper(jumper_x)

        pygame.display.update()

        clock.tick(15)

        if lives_count <= 0:#game ends if your lives count hits 0
            game_close = True

    pygame.quit()
    quit()


game_loop()
