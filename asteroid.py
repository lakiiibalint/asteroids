from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame
from constants import ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
       self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        angle = random.uniform(20,50)

        new_vector_A = self.velocity.rotate(angle)
        new_vector_B  = self.velocity.rotate(-angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        Asteroid_A = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid_A.velocity = new_vector_A * 1.2
        Asteroid_B = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid_B.velocity = new_vector_B * 1.2