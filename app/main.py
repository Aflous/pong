import pygame
from ball import Ball
from constants import (
    BALL_RADIUS,
    FPS,
    HEIGHT,
    PADDLE_HEIGHT,
    PADDLE_WIDTH,
    SCORE_FONT,
    WHITE,
    WIDTH,
    WIN,
    WINNING_SCORE,
)
from paddle import Paddle

pygame.display.set_caption("Pong")


def draw(win: pygame.Surface, paddles: list[Paddle], ball: Ball, left_score: int, right_score: int) -> None:
    """Draw everything to screen"""

    left_score_text = SCORE_FONT.render(f"{left_score}", True, WHITE)
    right_score_text = SCORE_FONT.render(f"{right_score}", True, WHITE)
    win.blit(left_score_text, (WIDTH // 4 - left_score_text.get_width() // 2, 20))
    win.blit(right_score_text, (WIDTH * (3 / 4) - right_score_text.get_width() // 2, 20))

    for paddle in paddles:
        paddle.draw(win)

    for i in range(10, HEIGHT, HEIGHT // 20):
        if i % 2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH // 2 - 5, i, 10, HEIGHT // 20))

    ball.draw(win)
    pygame.display.update()


def handle_collision(ball: Ball, left_paddle: Paddle, right_paddle: Paddle) -> None:
    """Handle collision between ball and paddles"""
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1
    elif ball.y - ball.radius <= 0:
        ball.y_vel *= -1

    def change_direction(paddle: Paddle) -> None:
        """Change direction of ball"""
        ball.x_vel *= -1
        middle_y = paddle.y + paddle.height / 2
        difference_in_y = middle_y - ball.y
        reduction_factor = (paddle.height / 2) / ball.MAX_VEL
        y_vel = difference_in_y / reduction_factor
        ball.y_vel = -1 * y_vel

    if ball.x_vel < 0:
        if left_paddle.y <= ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                change_direction(left_paddle)

    else:
        if right_paddle.y <= ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                change_direction(right_paddle)


def handle_paddle_movement(keys: tuple[bool, ...], left_paddle: Paddle, right_paddle: Paddle) -> None:

    """Handle paddle movement"""
    for up, down, paddle in [(pygame.K_w, pygame.K_s, left_paddle), (pygame.K_UP, pygame.K_DOWN, right_paddle)]:
        if keys[up] and paddle.y - paddle.VEL >= 0:
            paddle.move(up=True)
        if keys[down] and paddle.y + paddle.VEL + paddle.height <= HEIGHT:
            paddle.move(up=False)


def main() -> None:

    background = pygame.image.load("assets/background.png")
    pygame.mixer.music.load("assets/cipher.mp3")
    # Set the volume of the music (optional)
    pygame.mixer.music.set_volume(0.3)
    # Play the background music on a loop
    pygame.mixer.music.play(-1)

    run = True

    clock = pygame.time.Clock()
    left_paddle = Paddle(10, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

    left_score = 0
    right_score = 0

    while run:
        clock.tick(FPS)
        WIN.blit(background, (0, 0))
        draw(WIN, [left_paddle, right_paddle], ball, left_score, right_score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)

        ball.move()
        handle_collision(ball, left_paddle, right_paddle)

        if ball.x < 0:
            right_score += 1
            ball.reset()
        elif ball.x > WIDTH:
            left_score += 1
            ball.reset()

        if left_score >= WINNING_SCORE or right_score >= WINNING_SCORE:
            if left_score >= WINNING_SCORE:
                win_text = "Left Player Won!"
            else:
                win_text = "Right Player Won!"
            text = SCORE_FONT.render(win_text, True, WHITE)
            WIN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
            pygame.display.update()
            pygame.time.delay(5000)
            ball.reset()
            left_paddle.reset()
            right_paddle.reset()
            left_score = 0
            right_score = 0

    pygame.quit()


if __name__ == '__main__':
    main()
