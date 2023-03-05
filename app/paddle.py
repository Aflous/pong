import pygame

from constants import WHITE


class Paddle:
    COLOR: tuple[int, int, int] = WHITE
    VEL: int = 5

    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.width = width
        self.height = height

    def draw(self, win: pygame.Surface) -> None:

        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, up: bool = True) -> None:
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

    def reset(self) -> None:
        self.x = self.original_x
        self.y = self.original_y
