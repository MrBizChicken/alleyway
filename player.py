import pygame, random
from constants import *
import player

class Player(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.x = GAME_WIDTH // 2
        self.y = GAME_HEIGHT
        self.width = width
        self.height = height
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (self.x, self.y)





    def update(self):
        self.key_input()


    def key_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:

            if self.rect.x > 0:
                self.rect.x += -self.speed

        if keys[pygame.K_RIGHT]:
            if self.rect.left < GAME_WIDTH:
                self.rect.x += self.speed
