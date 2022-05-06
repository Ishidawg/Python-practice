import pygame
from pygame.display import update

# init
pygame.init()

# constant varibles
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
LIGHT_BLUE = (103, 186, 224)

# player
PLAYER_IMAGE = pygame.image.load('Character/Blue-char/sprite_wak0.png')

# title screen
pygame.display.set_caption("Project Adventure")

# main function and game loop
def main():

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # draw and update
        SCREEN.fill(LIGHT_BLUE)
        SCREEN.blit(PLAYER_IMAGE, (0, 0))
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__": #call others py files
    main()