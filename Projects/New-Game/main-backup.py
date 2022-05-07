from os import close
from typing import KeysView
import pygame
from pygame.display import update

# init
pygame.init()

# constant varibles
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
DARK_PURPLE = (72, 3, 156)
DARK_GREEN = (48, 102, 56)

# player
PLAYER_IMAGE = pygame.image.load('./Character/blue-ball.png')


# plataform

# first two values, refer to position
# second two values, refer to with/height of rect, in this case, plataform

PLATAFORMS = [
    # PLATAFORM
    pygame.Rect (200, 250, 400, 50),
    # LEFT
    pygame.Rect (200, 200, 50, 50),
    # RIGHT
    pygame.Rect ( 550, 200, 50, 50)
]

# title screen
pygame.display.set_caption("Project New Game")

# main function and game loop
def main():
    # player x position
    PLAYERX = 360
    PLAYERY = 80

    # frame limit
    clock = pygame.time.Clock()

    run = True
    while run:
        fps_velocity = clock.tick(FPS)
        # inputs section [CENTRAL]

        # input - quit event
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.QUIT

        # input - player input
        KEYS = pygame.key.get_pressed()

        if KEYS[pygame.K_a]:
            PLAYERX -= 1 * fps_velocity
        
        if KEYS[pygame.K_d]:
            PLAYERX += 1 * fps_velocity

        if KEYS[pygame.K_w]:
            PLAYERY -= 1 * fps_velocity

        if KEYS[pygame.K_s]:
            PLAYERY += 1 * fps_velocity

        # draw and update
        SCREEN.fill(DARK_PURPLE)

        for plat in PLATAFORMS:
            pygame.draw.rect(SCREEN, DARK_GREEN, plat)

        SCREEN.blit(PLAYER_IMAGE, (PLAYERX, PLAYERY))
        pygame.display.update()

    pygame.quit()

#call others py files
if __name__ == "__main__":
    main()