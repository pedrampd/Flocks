import pygame, sys
from boid import Boid
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root

DATA = os.path.join(ROOT_DIR, "data")

WIDTH, HEIGHT = 1000, 800


def main():
    # init
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(
        (WIDTH, HEIGHT)
    )  # , pygame.FULLSCREEN, pygame.RESIZABLE)
    background = pygame.image.load(os.path.join(DATA, "bg.png"))
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    background.convert()

    # groups
    boid_group = pygame.sprite.Group()
    for i in range(15):
        boid = Boid(os.path.join(DATA, "boid32x32.png"))
        boid_group.add(boid)

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        screen.blit(background, (0, 0))
        boid_group.draw(screen)
        boid_group.update()

        clock.tick(60)


if __name__ == "__main__":
    main()
