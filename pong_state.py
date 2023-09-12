class PongState:
    """Class to represent the state of a Pong game."""
    
    def __init__(self, ball_x, ball_y, ball_vel_x, ball_vel_y, paddle_y):
        """Initialize the Pong game's state.
        
        Parameters:
            ball_x (float): Horizontal position of the ball.
            ball_y (float): Vertical position of the ball.
            ball_vel_x (float): Horizontal velocity of the ball.
            ball_vel_y (float): Vertical velocity of the ball.
            paddle_y (float): Vertical position of the paddle.
        """
        self.ball_x = ball_x
        self.ball_y = ball_y
        self.ball_vel_x = ball_vel_x
        self.ball_vel_y = ball_vel_y
        self.paddle_y = paddle_y

    def state_to_list(self):
        """Convert the current game state into a list.
        
        Returns:
            list: Contains ball's position, velocities, and paddle's position.
        """
        return [self.ball_x, self.ball_y, self.ball_vel_x, self.ball_vel_y, self.paddle_y]

    def __str__(self):
        """Return a human-readable string representation of the game state.
        
        Returns:
            str: Descriptive state of the ball's position, velocity, and paddle's position.
        """
        return f"Ball Position: ({self.ball_x}, {self.ball_y}), Ball Velocity: ({self.ball_vel_x}, {self.ball_vel_y}), Paddle Y: {self.paddle_y}"