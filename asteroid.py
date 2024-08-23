import pygame
import random
from circleshape import CircleShape
from typing import Tuple

from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    containers: Tuple[pygame.sprite.Group, ...] = ()
    def __init__(self, x, y, radius):
        self.radius = radius
        self.position = pygame.Vector2(x,y)
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,center = self.position #[self.x,self.y]
                           ,color=[255,255,255]
                           ,radius= self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        aster1 = Asteroid(self.position.x, self.position.y, new_radius)
        aster1.velocity = self.velocity.rotate(rand_angle) * 1.2

        aster2 = Asteroid(self.position.x, self.position.y, new_radius)
        aster2.velocity = self.velocity.rotate(-rand_angle) * 1.2



