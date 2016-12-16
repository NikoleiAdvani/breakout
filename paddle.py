# Nikolei Advani, 12/16/2016
# This class creates the paddle
import pygame
class Paddle(pygame.sprite.Sprite):

    def __init__(self, color):
        super().__init__()
        self.WIDTH = 60
        self.HEIGHT = 10
        self.color = color
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.rect = self.image.get_rect()
        self.image.fill(self.color)
    # This method allows the paddle to move along the x axis within the screen
    def move(self, width):
       draw = pygame.mouse.get_pos()[0]
       self.rect.x = draw
       if draw + self.WIDTH >= width:
           self.rect.x = 350




