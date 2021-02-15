import pygame, random
from constants import *
import player
pygame.init()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = GAME_WIDTH // 2
        self.y = 300
        self.width = 200
        self.height = 30
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)





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
