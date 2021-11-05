from typing import Any
import pygame

def ImageNotFound(Exception):
    pass


class Boid(pygame.sprite.Sprite):
    def __init__(self, posx :int, posy:int, path ) -> None:
        super().__init__()
        self.x = posx
        self.y = posy
        self._image = pygame.image.load(path)
        self.rect = self._image.get_rect()

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self,path):
        try:
            self._image = pygame.image.load(path)
        except ImageNotFound as e:
            raise e(f'image not found at {path}')
    
    def update(self) -> None:
        self.rect.center = pygame.mouse.get_pos()

