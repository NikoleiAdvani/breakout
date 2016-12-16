# Nikolei Advani, 12/16/2016
# This program runs the game 'breakout'
import ball
import brick
import paddle
import pygame
import sys
from pygame.locals import *


def main():
    pygame.font.init()
    pygame.display.set_caption("BREAKOUT")
    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4 # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH =  (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    NUM_TURNS = 3
    myFont = pygame.font.SysFont("Helvetica", 24)
    # The following lines of code create the pygame window and two sprite groups
    window = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    blocksGroup = pygame.sprite.Group()
    paddleGroup = pygame.sprite.Group()

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    PINK = (255, 20, 147)
    # Puts colors in a list and assigns x and y coordinates for bricks
    colors = [RED, RED, ORANGE, ORANGE, YELLOW, YELLOW, GREEN, GREEN, CYAN, CYAN]
    xPos = BRICK_SEP
    yPos = BRICK_Y_OFFSET
    # This for loop creates the array of bricks on the screen
    for x in range(10):
        for y in range(BRICKS_PER_ROW):
            row_of_bricks = brick.Brick(BRICK_WIDTH, colors[x])
            row_of_bricks.rect.x = xPos
            row_of_bricks.rect.y = yPos
            blocksGroup.add(row_of_bricks)
            window.blit(row_of_bricks.block, row_of_bricks.rect)
            xPos += BRICK_WIDTH + BRICK_SEP
        yPos += BRICK_SEP + 8
        xPos = BRICK_SEP
    # The following lines of code create and blit the paddle on the screen
    my_paddle = paddle.Paddle(WHITE)
    my_paddle.rect.x = APPLICATION_WIDTH / 2
    my_paddle.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    paddleGroup.add(my_paddle)
    window.blit(my_paddle.image, my_paddle.rect)
    # The following lines of code create and blit the ball on the screen
    my_ball = ball.Ball(PINK, APPLICATION_WIDTH, APPLICATION_HEIGHT)
    my_ball.rect.x = APPLICATION_WIDTH / 2
    my_ball.rect.y = APPLICATION_HEIGHT / 2
    window.blit(my_ball.image2, my_ball.rect)
    # label prints 'GAME OVER' on the screen if you lose
    label = myFont.render("GAME OVER", 1, ORANGE)

    pygame.display.update()
    # This while loop ultimately makes the game play
    while NUM_TURNS >= 0:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        window.fill(BLACK)
        # This for loop continuously blits the blocks on the screen and makes the paddle and ball move
        for x in blocksGroup:
            window.blit(x.block, x.rect)
            my_paddle.move(APPLICATION_WIDTH)
        window.blit(my_paddle.image, my_paddle.rect)
        my_ball.move()
        my_ball.collideBricks(blocksGroup)
        my_ball.collidePaddle(paddleGroup)
        # This if statement subtracts a life from gameplay if your ball hits the bottom of the screen
        if my_ball.rect.bottom >= APPLICATION_HEIGHT:
            my_ball.rect.x = APPLICATION_WIDTH / 2
            my_ball.rect.y = APPLICATION_HEIGHT / 2
            NUM_TURNS -= 1
        window.blit(my_ball.image2, my_ball.rect)
        pygame.display.update()
        # This if statement prints "GAME OVER" on the screen if you lose
        if NUM_TURNS == 0:
            window.blit(label, (APPLICATION_WIDTH / 2, APPLICATION_HEIGHT / 2))
            pygame.display.update()
            pygame.time.wait(2000)
            break




main()
