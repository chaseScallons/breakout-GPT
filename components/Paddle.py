import pygame

class Paddle:
    # White
    COLOR = (255, 255, 255)
    
    def __init__(self, x, y, width, height):
        """
        Initializes the paddle with a position, size, and speed.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 7

    def draw(self, screen):
        """
        Draws the paddle on the screen.
        """
        pygame.draw.rect(screen, self.COLOR, (self.x, self.y, self.width, self.height))

    def move(self, direction, screen_width):
        """
        Moves the paddle in the specified direction.
        """
        if direction == 'left' and self.x > 0:
            self.x -= self.speed
        elif direction == 'right' and self.x < screen_width - self.width:
            self.x += self.speed