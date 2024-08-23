import pygame
from circleshape import CircleShape
from typing import Tuple

class Shot(CircleShape):
    containers: Tuple[pygame.sprite.Group, ...] = ()
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(self.x,self.y)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen,[255,255,255]
                           ,center=self.position
                           ,radius=self.radius)


    def update(self, dt):
        self.position += self.velocity * dt
