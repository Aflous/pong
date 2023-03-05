import pygame

from constants import WHITE


class Ball:
    MAX_VEL: int = 5
    COLOR: tuple[int, int, int] = WHITE

    def __init__(self, x: int, y: int, radius: int) -> None:
        self.x = self.original_x = x
        self.y = self.original_y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    def draw(self, win: pygame.Surface) -> None:
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.radius)

    def move(self) -> None:
        self.x += self.x_vel
        self.y += self.y_vel

    def reset(self) -> None:
        self.x = self.original_x
        self.y = self.original_y
        self.y_vel = 0
        self.x_vel *= -1
