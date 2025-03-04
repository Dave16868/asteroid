import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS: 
            return
        else: 
            random_angle = random.uniform(20,50)
            v1 = self.velocity.rotate(random_angle)
            v2 = self.velocity.rotate(-random_angle)
            r = self.radius - ASTEROID_MIN_RADIUS

            baby_1 = Asteroid(self.position.x, self.position.y, r)
            baby_2 = Asteroid(self.position.x, self.position.y, r)

            baby_1.velocity = v1 * 1.2
            baby_2.velocity = v2 * 1.2

