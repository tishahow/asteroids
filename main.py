from player import Player
import pygame; from constants import SCREEN_WIDTH, SCREEN_HEIGHT; from logger import log_state

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        dt = clock.tick(60) / 1000
        #{dt})
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()

    
if __name__ == "__main__":
    main()
