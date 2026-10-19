import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from pygame import display
from player import Player
from shot import Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField 
from logger import log_event
import sys

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable) 
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (updatable, drawable, shots)
    AsteroidField.containers = (updatable)

    ast_field = AsteroidField()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for member in drawable:
            member.draw(screen)
        for member in updatable:
            member.update(dt)
        for object in asteroids:
            if object.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if shot.collides_with(asteroid):
                     log_event("asteroid_shot")
                     shot.kill()
                     asteroid.kill()
        
        display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()
