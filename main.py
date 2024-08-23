import sys
import pygame
from pygame.display import update
from asteroid import Asteroid
from asteroidfield import AsteroidField
from circleshape import CircleShape
from constants import *
from player import Player
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH,SCREEN_HEIGHT))
    game_time = pygame.time.Clock()
    pygame.display.set_caption('Astroids Game')

    #Crating groups
    allshots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()

    #adding classes groups to containers
    Player.containers = (updatable,drawable)
    Asteroid.containers = (updatable,drawable,all_asteroids)
    AsteroidField.containers = (updatable,)
    Shot.containers = (updatable,drawable,allshots)

    #instantiate 
    theplayer = Player(x = SCREEN_WIDTH/2, y = SCREEN_HEIGHT/2)
    theasteroid = Asteroid(x=0,y=0,radius=0)
    theasteroidfield = AsteroidField()

    background = pygame.image.load('assets/space_background.png').convert()
    font = pygame.font.Font(None,40)
    game_over_txt = font.render('Game Over macha!',True,(255,255,255))


    # updatable.add(theasteroid)
    # updatable.add(theplayer,theasteroid,theasteroidfield)
    # drawable.add(theplayer,theasteroid)
    # all_asteroids.add(theasteroid)
    dt = 0
    game_over = False

    # GAME LOOP ____STARTS_____----____--____#
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.blit(background,(0,0))


        ##screen.fill(color=(0,0,0))
        #
        for item in updatable:
            item.update(dt)

        for item in drawable:
            item.draw(screen)

        for item in all_asteroids:

            if theplayer.isColliding(item):
                game_over = True
                screen.blit(game_over_txt,(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
                pygame.display.flip()

                while game_over:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                pygame.quit()
                                sys.exit()
                            elif event.key == pygame.K_r:
                                item.kill()
                                game_over = False
                                break
                    pygame.time.Clock().tick(5)


            for shot in allshots:
                if shot.isColliding(item):
                    item.split()
                    shot.kill()


        pygame.display.flip()
        dt = game_time.tick(60) / 1000

    # GAME LOOP ____ENDS_____----____--____#

if __name__ == "__main__":
    main()
