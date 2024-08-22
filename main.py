import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    game_time = pygame.time.Clock()
    #instantiate player
    theplayer = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    background = pygame.image.load('assets/space_background.png').convert()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    updatable.add(theplayer)
    drawable.add(theplayer)

    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background,(0,0))


        # screen.fill(color=(0,0,0))
        #
        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        pygame.display.flip()
        dt = game_time.tick(60) / 1000


if __name__ == "__main__":
    main()
