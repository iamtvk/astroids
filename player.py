import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_SPEED, PLAYER_TURN_SPEED

class Player(CircleShape):
    def __init__(self, x, y) -> None:
        self.radius = PLAYER_RADIUS
        super().__init__(x,y,self.radius)
        # self.x = x
        # self.y = y
        self.position = pygame.Vector2(x,y)
        self.rotation = 0

    containers  = ()

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a,b,c]


    def draw(self, screen) -> None:
        pygame.draw.polygon(screen,(255,255,255)
                            ,self.triangle()
                            ,width=2)

    def rotate(self,dt) -> None:
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        #Vim controls
        # if keys[pygame.K_l]:
        #     self.rotate(dt)
        #
        # if keys[pygame.K_h]:
        #     self.rotate(-dt)
        #
        # if keys[pygame.K_k]: #forward
        #     self.move(dt)
        #
        # if keys[pygame.K_j]:
        #     self.move(-dt)

        # WASD controls
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_w]: #forward
            self.move(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt 
        #distance = directionVect * speed * time(something like that)








