from os import close
from typing import KeysView
import pygame
from pygame.display import update

# init
pygame.init()
clock = pygame.time.Clock()

# constant varibles
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
DARK_PURPLE = (72, 3, 156)
LIGHT_GREEN = (176, 232, 210)

# player
PLAYER_IMAGE = pygame.image.load('./Character/White-square.png')


# plataform

# first two values, refer to position
# second two values, refer to with/height of rect, in this case, plataform

PLATAFORMS = [
    # PLATAFORM
    pygame.Rect (200, 250, 400, 50),
    # LEFT
    pygame.Rect (200, 200, 50, 50),
    # RIGHT
    pygame.Rect (550, 200, 50, 50)
]

# title screen
pygame.display.set_caption("Project New Game")

# main function and game loop
def main():
    # player x position
    PLAYERX = 360
    PLAYERY = 140
    PLAYER_SPEED = 0
    PLAYER_ACC = 1


    run = True
    while run:
        # inputs section [CENTRAL]

        # input - quit event
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    pygame.QUIT

        NEW_PLAYERX = PLAYERX
        NEW_PLAYERY = PLAYERY

        # input - player input
        KEYS = pygame.key.get_pressed()


        if KEYS[pygame.K_a]:
            NEW_PLAYERX -= 2
        
        if KEYS[pygame.K_d]:
            NEW_PLAYERX += 2

        PLAYER_SPEED += PLAYER_ACC

        if KEYS[pygame.K_w]:
            NEW_PLAYERY -= 2

        if KEYS[pygame.K_s]:
            NEW_PLAYERY += 2

        # horizontal movement
        NEW_PLAYER_RECT = pygame.Rect(NEW_PLAYERX, NEW_PLAYERY, 100, 100)
        XCOLLISION = False

        # vertical movement
        YCOLLISION = False

        # check plataforms
        for plat in PLATAFORMS:
            if plat.colliderect(NEW_PLAYER_RECT):
                XCOLLISION = True
                break

        if XCOLLISION == False:
            PLAYERX = NEW_PLAYERX

        for plat in PLATAFORMS:
            if plat.colliderect(NEW_PLAYER_RECT):
                YCOLLISION = True
                break

        if YCOLLISION == False:
            PLAYERY = NEW_PLAYERY

        # draw and update
        SCREEN.fill(DARK_PURPLE)

        for plat in PLATAFORMS:
            pygame.draw.rect(SCREEN, LIGHT_GREEN, plat)

        SCREEN.blit(PLAYER_IMAGE, (PLAYERX, PLAYERY))
        pygame.display.update()

        clock.tick(60)

    pygame.quit()

#call others py files
if __name__ == "__main__":
    main()