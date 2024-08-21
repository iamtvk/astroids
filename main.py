import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


        screen.fill(color=(143,188,187))
        pygame.display.flip()


if __name__ == "__main__":
    main()
