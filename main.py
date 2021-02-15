from constants import *
import pygame
import player
import ball
import bricks
pygame.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))

pygame.init()

player_group = pygame.sprite.Group()
bricks_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()

player = player.Player()
bricks = bricks.Bricks()
ball = ball.Ball()

player_group.add(player)
bricks_group.add(bricks)
ball_group.add(ball)








def main():
    running = True

    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()

        draw()
        update()

    pygame.quit()




def draw():
    surface.fill((0, 0, 0))
    player_group.draw(surface)
    bricks_group.draw(surface)
    ball_group.draw(surface)



    pygame.display.flip()


def update():
    ball_group.update()
    player_group.update()
    bricks_group.update()








if __name__ == "__main__":
    main()
