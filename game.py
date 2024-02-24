import pygame
from components.Paddle import Paddle
from components.Ball import Ball, check_ball_paddle_collision, check_ball_block_collisions
from components.Blocks import Block  # Ensure this matches the actual file and class names

# Initialize Pygame
pygame.init()

# Game window/screen constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Game colors
BLACK = (0, 0, 0)

def create_blocks(rows, columns, block_height, offset_y, gap):
    total_gap_width = (columns + 1) * gap
    available_width = SCREEN_WIDTH - total_gap_width
    block_width = available_width // columns
    offset_x = (SCREEN_WIDTH - (columns * block_width + total_gap_width)) // 2

    blocks = []
    for row in range(rows):
        for col in range(columns):
            x = offset_x + col * (block_width + gap) + gap
            y = offset_y + row * (block_height + gap) + gap
            blocks.append(Block(x, y, block_width, block_height))
    return blocks

def reset_game(ball, paddle, blocks):
    # Reset ball to the starting position
    ball.x = SCREEN_WIDTH // 2
    ball.y = SCREEN_HEIGHT - 40
    ball.vel_x = Ball.DEFAULT_VEL_X
    ball.vel_y = -Ball.DEFAULT_VEL_Y
    
    # Reset paddle to the starting position
    paddle.x = SCREEN_WIDTH // 2 - paddle.width // 2
    paddle.y = SCREEN_HEIGHT - 30
    
    # Recreate blocks for a full game reset
    blocks[:] = create_blocks(5, 8, 20, 50, 10)

def main():
    paddle = Paddle(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 30, 100, 10)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40, 10)
    blocks = create_blocks(5, 8, 20, 50, 10)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move('left', SCREEN_WIDTH)
        if keys[pygame.K_RIGHT]:
            paddle.move('right', SCREEN_WIDTH)

        ball.move(SCREEN_WIDTH, SCREEN_HEIGHT)
        if ball.y + ball.radius > SCREEN_HEIGHT:  # Check for ball missing the paddle
            reset_game(ball, paddle, blocks)  # Reset the game

        check_ball_paddle_collision(ball, paddle)
        hit_blocks = check_ball_block_collisions(ball, blocks)

        for block in hit_blocks:
            blocks.remove(block)

        screen.fill(BLACK)
        paddle.draw(screen)
        ball.draw(screen)
        for block in blocks:
            if not block.hit:
                block.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()