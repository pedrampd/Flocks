from typing import Any
import pygame
import numpy as np
import math

def ImageNotFound(Exception):
    pass


WIDTH, HEIGHT = 1000, 800


class BaseBoid(pygame.sprite.Sprite):
    def __init__(self, image_path) -> None:
        super().__init__()
        self.deltaR = 2.0
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH * np.random.random()
        self.rect.centery = HEIGHT * np.random.random()
        self.speed_vector = [4, 4]


class Boid(BaseBoid):
    def __init__(self, image_path) -> None:
        super().__init__(image_path)
        self.image_path = image_path

    def boundary_condition(self):
        x = self.rect.centerx
        y = self.rect.centery

        if x > WIDTH + self.deltaR:
            x = - self.deltaR
        elif x < -self.deltaR:
            x = WIDTH + self.deltaR
        if y > HEIGHT + self.deltaR:
            y = - self.deltaR
        elif y < -self.deltaR:
            y = HEIGHT + self.deltaR
        self.rect.centerx = x
        self.rect.centery = y

    def update(self) -> None:
        angle = math.atan(self.speed_vector[1] / self.speed_vector[0])
        angle = (180 / np.pi) * angle - 180
        image = pygame.image.load(self.image_path)
        self.image = pygame.transform.rotate(image, angle)
        # self.rect = self.image.get_rect()
        self.rect.centerx += self.speed_vector[0]
        self.rect.centery += self.speed_vector[1]
        self.boundary_condition()
