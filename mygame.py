import pygame
import random
from time import sleep

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

perper = (233,33,255)
green_low = (22,148,42)
red_low = (148,22,42)

display_IMG = pygame.image.load('E://python//my game.py//img//Kitty.png')


gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('خرگوش')
pygame.display.set_icon(display_IMG)

clock = pygame.time.Clock()

carImg = pygame.image.load('E://python//my game.py//IMG//22253-rabbit-face-icon.png')
thingImg = pygame.image.load('E://python//my game.py//img//Kitty.png')
heartImg = pygame.image.load('E://python//my game.py//img//heart.png')
shop = pygame.image.load('E:\merged_partition_content\my download\shop-icon.png')

List_IMG = [car_1 , car_2 ,car_3 , car_4 , car_5 , car_6 , car_7 , car_8 , car_9]

pygame.mixer.music.load("E:\python\My Game.py\MP3\world-m.ogg")

car_width = 64

def show_all_img (IMG , x , y):
    gameDisplay.blit(IMG , (x , y))

def start_shop ():
    print ('OK')

def show_shop (x,y):
    h , w = 128 , 128
    gameDisplay.blit(shop , (x,y))
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()


    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == True:
            start_shop()

def button_IMG(IMG,x,y):
    h , w = 64 , 64
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    show_all_img (IMG , x , y)
    pygame.display.update()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        if click[0] == 1:
            return 'ok'


def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            pygame.mixer.music.play(1)
            action()


    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    TextSurf,TextRect = text_objects(msg,smallText)
    TextRect.center = ((x+(w/2)),(y + (h/2)))
    gameDisplay.blit(TextSurf,TextRect)

def quitgame():
    pygame.quit()
    exit()

def game_intro():
    intro = True

    while intro:
        gameDisplay.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.K_KP_ENTER:
                game_loop()
        show_shop(672,-12)

        largeText = pygame.font.Font('freesansbold.ttf',90)
        TextSurf, TextRect = text_objects("Let's Play Game",largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf,TextRect)
        
        button("Play!",150,450,100,50,green,green_low,game_loop)
        button("Quit",550,450,100,50,red,red_low,quitgame)

        pygame.display.update()


def game_loop():
    gameDisplay.fill( perper )
    heart_counter = 3
    counter = 0
    x_change = 0

    x = (display_width * 0.45)
    y = (display_height * 0.8)   

    stuff_startx = x + 1
    stuff_starty = -700
    stuff_speed = 7
    stuff_width = 64
    stuff_height = 54

    gameExit = False

    pygame.mixer.music.play(-1)

    while not gameExit:
        gameDisplay.fill( perper )

        for event in pygame.event.get(): # event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -7
                elif event.key == pygame.K_RIGHT:
                    x_change = 7
                if event.key == pygame.K_s:
                    setjdfug = True
                    while setjdfug:
                        for event in pygame.event.get():
                            if event.type == pygame.KEYDOWN:
                                setjdfug = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_q:
                    with open ('E://python//my game.py//erfan.csv' , 'a+') as FILE_SCORE:
                        FILE_SCORE.write('\n')
                        FILE_SCORE.write(str(counter))
                        FILE_SCORE.close()
                    pygame.quit()
                    quit()


        x += x_change
        
        stuff_starty += stuff_speed


        # stuffx , stuffy
        stuff ( stuff_startx , stuff_starty )

        Show_car(x,y)
        if x > display_width - car_width or x < 0: # out of page
            stuff_startx = x + 1
            stuff_starty = -700
            stuff ( stuff_startx , stuff_starty )
            heart_counter -= 1
            
            if heart_counter == 0:
                crash()
            
        stuff_dodged (counter)

        if stuff_starty > display_height: # score
            stuff_starty = 0 - stuff_height
            stuff_startx = x + 1
            counter += 1
            if counter % 5 == 0:
                stuff_speed += 1
                if counter == 100:
                    message_display_text('GAD OF GAME!!!')
                    sleep(3)
        
        if y < stuff_starty + stuff_height: # crash
            if x > stuff_startx and x < stuff_startx + stuff_width or x + car_width > stuff_startx and x + car_width < stuff_startx + stuff_width:
                
                stuff_startx = x + 1
                stuff_starty = -700
                stuff ( stuff_startx , stuff_starty )
                heart_counter -= 1
                
                if heart_counter == 0:
                    crash()
                else:
                    message_display('YOU CRASHED')


        Show_heart(heart_counter , display_width)

        pygame.display.update()
        clock.tick(60)


def Show_heart (heart_count , display_width):
    if heart_count == 3:
        gameDisplay.blit (heartImg , (display_width - 30,0))
        gameDisplay.blit (heartImg , (display_width - 60,0))
        gameDisplay.blit (heartImg , (display_width - 90,0))
    elif heart_count == 2:
        gameDisplay.blit (heartImg , (display_width - 30,0))
        gameDisplay.blit (heartImg , (display_width - 60,0))
    elif heart_count == 1:
        gameDisplay.blit (heartImg , (display_width - 30,0))

def message_display_text(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

def stuff_dodged(count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("score : "+str(count) , True , black)
    gameDisplay.blit(text,(0,0))

def stuff(stuffx,stuffy):
    gameDisplay.blit(thingImg , (stuffx , stuffy))

def Show_car(x,y):
    gameDisplay.blit (carImg , ( x , y ))

def text_objects(text,font):
    textSurface = font.render(text, True , black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',90)
    TextSurf, TextRect = text_objects(text,largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()

    sleep(2)

game_intro()
