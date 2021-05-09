import pygame, random
from constants import *
import player
pygame.init()
class Ball(pygame.sprite.Sprite):
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
        self.rect.midbottom = (self.x, self.y - self.height)
        self.horz_speed = 6
        self.vert_speed = 6
        self.lives = 5








    def update(self, bricks_group, player_group):
        self.move()
        if pygame.sprite.spritecollide(self, player_group, False):
            self.vert_speed = -self.vert_speed

        hit_bricks = pygame.sprite.spritecollide(self, bricks_group, False)
        if hit_bricks:
            self.vert_speed = -self.vert_speed
            for b in hit_bricks:
                b.health -= 1

        if self.rect.bottom >= GAME_HEIGHT:
            self.lives -=1

        if self.lives == -1:
            self.lives = 5













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
