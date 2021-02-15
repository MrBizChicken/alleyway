import pygame, random
from constants import *
import player
pygame.init()
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 300
        self.y = 300
        self.width = 64
        self.height = 64
        self.speed = 5
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill((255, 255 ,255))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.horz_speed = 3
        self.vert_speed = 3





    def update(self, player_group):
        self.move()
        if pygame.sprite.spritecollide(self, player_group, False):
            self.vert_speed = -self.vert_speed








    def move(self):
        self.rect = self.rect.move(-self.horz_speed, self.vert_speed)
        if self.rect.right >= GAME_WIDTH:
            self.horz_speed = -self.horz_speed
            self.vert_speed + self.vert_speed


        if self.rect.x < 0:
            self.horz_speed = - self.horz_speed
            self.vert_speed + self.vert_speed




        if self.rect.bottom >= GAME_HEIGHT:
            self.horz_speed + self.horz_speed
            self.vert_speed = -self.vert_speed
        if self.rect.top <= 0:
            self.horz_speed + self.horz_speed
            self.vert_speed = -self.vert_speed
