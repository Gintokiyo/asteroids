import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)

    starting_x = SCREEN_WIDTH / 2
    starting_y = SCREEN_HEIGHT / 2
    player = Player(starting_x, starting_y)
    asteroid_field = AsteroidField()

    while(1):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                
            for obj in updatable:
                 obj.update(dt)

            for obj in asteroids:
                 if obj.collision(player):
                      print("Game over!")
                      sys.exit()
            screen.fill("black")

            for obj in drawable:
                 obj.draw(screen)
            pygame.display.flip()
            dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
