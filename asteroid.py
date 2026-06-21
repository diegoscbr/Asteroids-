from circleshape import CircleShape
from constants import *
from logger import log_event
import pygame
import random
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
        
    def update(self, dt):
        velocity = self.velocity
        self.position += (velocity * dt)
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS: return
        log_event("asteroid_split")
        angle = random.uniform(20,50)
        dir_1 = self.velocity.rotate(angle)
        dir_2 = self.velocity.rotate(-angle)
        rad = self.radius - ASTEROID_MIN_RADIUS
        sub_1 = Asteroid(self.position.x, self.position.y, rad)
        sub_2 = Asteroid(self.position.x, self.position.y, rad)
        sub_1.velocity = dir_1 * 1.2
        sub_2.velocity = dir_2 * 1.2

        

