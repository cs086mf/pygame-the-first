import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0,255,0)
blue = (0,0,255)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Slither')



clock = pygame.time.Clock()

#block_speed =20 #how many pixels the block moves per frame
block_size = 10 #how big the snake is -NOT length
apple_size = 10
FPS = 15

font = pygame.font.SysFont(None, 25)

def snake( block_size, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, black, [XnY[0], XnY[1], block_size, block_size])

def message_to_screen(msg, color):
    text_surf = font.render(msg, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = (display_width/2), (display_height/2)
    gameDisplay.blit(text_surf, text_rect)

def gameLoop():
    gameExit = False
    gameOver = False

    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []# it is here so the list is not constantly reset everytime it runs the section of code below
    snakeLength = 1

    appleX = round(random.randrange(0, display_width - block_size))
    appleY = round(random.randrange(0, display_height - block_size))


    while not gameExit:


        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Press C to try again, Q to quit", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_q:
                        gameExit = True
                        gameOver = False #to leave the while loop
                    if event.key == pygame.K_c:
                        gameLoop()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True


        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)


        pygame.draw.rect(gameDisplay, red, [appleX, appleY, apple_size, apple_size])


        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        snake(block_size, snakeList)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachsegment in snakeList [:-1]:
            if eachsegment  == snakeHead:
                gameOver = True

        pygame.display.update()

        #if lead_x >= appleX and lead_x <= appleX + apple_size:
         #   if lead_y >= appleY and lead_y <= appleY + apple_size:
          #      appleX = round(random.randrange(0, display_width - block_size))
           #     appleY = round(random.randrange(0, display_height - block_size))
            #    snakeLength += 1
        if lead_x > appleX and lead_x < appleX + apple_size or lead_x + block_size > appleX and lead_x + block_size < appleX + apple_size: #x crossover

            if lead_y > appleY and lead_y < appleY +apple_size or lead_y + block_size > appleY and lead_y +block_size < appleY + apple_size:
                appleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                appleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                snakeLength += 1

            elif lead_y + block_size > appleY and lead_y + block_size < appleY + apple_size:

                appleX = round(random.randrange(0, display_width - block_size))  # /10.0)*10.0
                appleY = round(random.randrange(0, display_height - block_size))  # /10.0)*10.0
                snakeLength += 1

                clock.tick(FPS)


    pygame.quit()
    quit()
gameLoop()