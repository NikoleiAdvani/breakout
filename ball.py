# Nikolei Advani, 12/16/2016
# This class creates the ball
import pygame
import random

class Ball(pygame.sprite.Sprite):

    def __init__(self, color, windowWidth, windowHeight):
        super().__init__()
        self.RADIUS = 10
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.image2 = pygame.Surface((self.RADIUS, self.RADIUS))
        self.rect = self.image2.get_rect()
        self.image2.fill(self.color)
        self.vx = random.randint(1, 3)
        if random.random() > 0.5:
            self.vx = -self.vx
        self.vy = 5

    # This method tells the ball how to move
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.x > self.windowWidth or self.rect.x < 0:
            self.vx = -self.vx
        if self.rect.y > self.windowHeight or self.rect.y < 0:
            self.vy = -self.vy
    # This method takes a brick away from the sprite group if it is hit and changes the direction of the ball
    def collideBricks(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, True):
            self.vy = -self.vy
    # This method allows the ball to bounce off of the paddle
    def collidePaddle(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.vy = -self.vy



