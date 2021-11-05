import pygame, sys
from boid import Boid
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root

DATA = os.path.join(ROOT_DIR, 'data')


def main():
    #init
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((800, 500))#, pygame.FULLSCREEN, pygame.RESIZABLE)
    background = pygame.image.load(os.path.join(DATA,'bg.png'))
    background = pygame.transform.scale(background, (800, 500))
    background.convert()

    #groups
    boid = Boid(0, 0, os.path.join(DATA, 'boid32x32.png'))
    boid_group = pygame.sprite.Group()
    boid_group.add(boid)

    #Main loop
    while True:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                sys.exit()


        pygame.display.flip()
        screen.blit(background, (0,0))
        boid_group.draw(screen)
        boid_group.update()

        clock.tick(60)

if __name__== "__main__":
    main()
