# Nikolei Advani, 12/16/2016
# This class creates the bricks
import pygame
class Brick(pygame.sprite.Sprite):

    def __init__(self, width, color):
        super().__init__()
        self.BRICK_HEIGHT = 8
        self.width = width
        self.color = color
        self.block = pygame.Surface((self.width, self.BRICK_HEIGHT))
        self.rect = self.block.get_rect()
        self.block.fill(self.color)
