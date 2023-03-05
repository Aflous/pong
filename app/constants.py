import pygame

pygame.init()

WIDTH: int = 700
HEIGHT: int = 500
WIN: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))
FPS: int = 60
WHITE: tuple[int, int, int] = (255, 255, 255)
BLACK: tuple[int, int, int] = (0, 0, 0)
PADDLE_WIDTH: int = 20
PADDLE_HEIGHT: int = 100
BALL_RADIUS: int = 7
SCORE_FONT: pygame.font.Font = pygame.font.SysFont("comicsans", 50)
WINNING_SCORE: int = 10
