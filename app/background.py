import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self) -> None:
        self.image = pygame.image.load("assets/background.png").convert()
