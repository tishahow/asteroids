from player import Player
import pygame; 
from constants import SCREEN_WIDTH, SCREEN_HEIGHT; 
from logger import log_state
from asteroids import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    asteroidfield = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        dt = clock.tick(60) / 1000
        #{dt})
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        screen.fill("black")
        for thing in drawable:
            thing.draw(screen)
        #player.draw(screen)
        updatable.update(dt)
        for item in asteroids:
            if item.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        pygame.display.flip()

    
if __name__ == "__main__":
    main()
