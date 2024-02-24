import pygame

class Ball:
    COLOR = (255, 255, 255)  # White
    DEFAULT_VEL_X = 3
    DEFAULT_VEL_Y = -3

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.vel_x = self.DEFAULT_VEL_X
        self.vel_y = self.DEFAULT_VEL_Y  # Now properly initializing velocities

    def draw(self, screen):
        pygame.draw.circle(screen, self.COLOR, (self.x, self.y), self.radius)

    def move(self, screen_width, screen_height):
        self.x += self.vel_x
        self.y += self.vel_y

        if self.x - self.radius <= 0 or self.x + self.radius >= screen_width:
            self.vel_x = -self.vel_x  # Corrected from self.DEFAULT_VEL_X to self.vel_x

        if self.y - self.radius <= 0:
            self.vel_y = -self.vel_y  # Corrected from self.DEFAULT_VEL_Y to self.vel_y

        # Optional: Handle ball hitting the bottom of the screen
        # if self.y + self.radius >= screen_height:
            # Reset the ball or trigger game over

def check_ball_paddle_collision(ball, paddle):
    ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)
    paddle_rect = pygame.Rect(paddle.x, paddle.y, paddle.width, paddle.height)
    if ball_rect.colliderect(paddle_rect):
        ball.vel_y = -ball.vel_y
        ball.y = paddle.y - ball.radius

def check_ball_block_collisions(ball, blocks):
    ball_rect = pygame.Rect(ball.x - ball.radius, ball.y - ball.radius, ball.radius * 2, ball.radius * 2)
    hit_blocks = []
    for block in blocks:
        if not block.hit:
            block_rect = pygame.Rect(block.x, block.y, block.width, block.height)
            if ball_rect.colliderect(block_rect):
                block.hit = True
                hit_blocks.append(block)
                ball.vel_y = -ball.vel_y
                break
    return hit_blocks