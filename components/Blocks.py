import pygame

class Block:
    COLOR = (255, 255, 255)  # Example color: green

    def __init__(self, x, y, width, height):
        """
        Initializes a block with a position, size, and hit state.
        
        :param x: The x-coordinate of the block's position.
        :param y: The y-coordinate of the block's position.
        :param width: The width of the block.
        :param height: The height of the block.
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hit = False  # Indicates whether the block has been hit.

    def draw(self, screen):
        """
        Draws the block on the screen if it hasn't been hit.
        
        :param screen: The Pygame screen to draw the block on.
        """
        if not self.hit:
            pygame.draw.rect(screen, self.COLOR, (self.x, self.y, self.width, self.height))