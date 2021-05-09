from constants import *
import pygame
import player
import ball
import bricks
pygame.init()
states = 0

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
surface = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
background_image = pygame.image.load("mothersday.png").convert()
background1_image = pygame.image.load("menu.png").convert()
background2_image = pygame.image.load("paused.png").convert()




pygame.init()

player_group = pygame.sprite.Group()
bricks_group = pygame.sprite.Group()
ball_group = pygame.sprite.Group()


#bricks = bricks.Bricks(x, y)

rows = 20
cols = 10
width = GAME_WIDTH // cols
height = (GAME_HEIGHT // 2)  // rows
gap = 1


player = player.Player(width * 3, height)
ball = ball.Ball(width // 4, height)
player_group.add(player)
ball_group.add(ball)

for c in range(cols):

    for r in range(rows):
        bricks_group.add(bricks.Bricks(c * width + (gap * c), r * height + (gap * r), width, height, 3))








def main():
    global states
    running = True


    while running:
        clock.tick(TICK_RATE)
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    pygame.quit()

                if event.key == pygame.K_p:

                    if states == 1:
                        states = 2

                    elif states == 2:
                        states = 1


                if event.key == pygame.K_SPACE:
                    if states == 0:
                        states = 1









        draw()
        update()

    pygame.quit()




def draw():
    global states


    if states == 0:
        menu()
    if states == 1:
        if ball.lives == 0:
            states = 0
            ball.lives = 5


        surface.blit(background_image, [0, 0])
        player_group.draw(surface)
        ball_group.draw(surface)
        bricks_group.draw(surface)
        draw_scores()


    # pause
    if states == 2:
        pause()



    pygame.display.flip()


def update():

    global states
    # main menu
    if states == 0:
        pass
    if states == 1:
        # if lives <= 0:
        #     states = 3

            ball_group.update(bricks_group, player_group)
            player_group.update()
            bricks_group.update()


# death
if states == 3:
    surface.fill((100, 100, 100))


def menu():
    surface.blit(background1_image, [0, 0])



def pause():
    surface.blit(background2_image, [0, 0])




def draw_scores():
    message_display(str(ball.lives), GAME_WIDTH / 2 - FONT_SIZE, FONT_SIZE)



def text_objects(text, font):
    textSurface = font.render(text, True, (255, 0, 0))
    return textSurface, textSurface.get_rect()



def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf',FONT_SIZE)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    surface.blit(TextSurf, TextRect)





if __name__ == "__main__":
    main()
