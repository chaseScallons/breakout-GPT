import turtle
from pong_state import PongState
from dqn_agent import Agent

# Constants
STATE_SIZE = 5  # Defined by PongState attributes: ball_x, ball_y, ball_vel_x, ball_vel_y, paddle_y
ACTION_SIZE = 2  # Paddle movement: Up or Down
BATCH_SIZE = 32
REWARD_HIT = 10  # Reward for hitting the ball
REWARD_MISS = -10  # Penalty for missing the ball

# Initialize the DQN agent
agent = Agent(STATE_SIZE, ACTION_SIZE)

def setup_window():
    """Configure and return the turtle window."""
    win = turtle.Screen()
    win.title("Pong")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)
    return win



def get_game_state():
    """Retrieve and return the current game state from the turtle objects."""
    return PongState(ball.xcor(), ball.ycor(), ball.dx, ball.dy, right_paddle.ycor())

# Window setup
win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Turn off screen updating for smoother animations

# Initialize left paddle with attributes
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=6, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Initialize right paddle with attributes
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=6, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Initialize ball with attributes
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1  # Initial horizontal velocity
ball.dy = -1  # Initial vertical velocity

# Define movement functions for both paddles
def left_paddle_up():
    """Move the left paddle upwards by 20 units, provided it's within the window boundaries."""
    y = left_paddle.ycor()
    if y < 250:
        left_paddle.sety(y + 20)

def left_paddle_down():
    """Move the left paddle downwards by 20 units, provided it's within the window boundaries."""
    y = left_paddle.ycor()
    if y > -240:
        left_paddle.sety(y - 20)

def right_paddle_up():
    """Move the right paddle upwards by 20 units, provided it's within the window boundaries."""
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 20)

def right_paddle_down():
    """Move the right paddle downwards by 20 units, provided it's within the window boundaries."""
    y = right_paddle.ycor()
    if y > -240:
        right_paddle.sety(y - 20)

# Set up keyboard bindings for paddle movement
win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

# Main game loop
while True:
    win.update()  # Refresh the screen

    # Retrieve the current game state
    state = get_game_state().state_to_list()

    # Let the agent decide the action based on current state
    action = agent.act(state)
    if action == 0:  # Move the paddle up
        right_paddle_up()
    else:  # Move the paddle down
        right_paddle_down()

    # Update ball's position based on its velocity
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for ball collisions and update rewards
    reward = 0  # Default reward
    done = False  # Flag to check if episode is finished

    # Border collision handling
    if ball.ycor() > 290 or ball.ycor() < -290:  # Top or bottom border
        ball.dy *= -1  # Invert vertical velocity

    # Right border (agent's goal post)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1  # Invert horizontal velocity
        reward = REWARD_MISS
        done = True

    # Left border
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle collision handling
    # Right paddle
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (right_paddle.ycor() + 50 > ball.ycor() > right_paddle.ycor() - 50):
        ball.color("blue")  # Change ball color for visualization
        ball.dx *= -1  # Invert horizontal velocity
        reward = REWARD_HIT

    # Left paddle
    elif (ball.dx < 0) and (-350 < ball.xcor() < -340) and (left_paddle.ycor() + 50 > ball.ycor() > left_paddle.ycor() - 50):
        ball.color("red")  # Change ball color for visualization
        ball.dx *= -1

    # Store the experience in the agent's memory
    next_state = get_game_state().state_to_list()
    agent.remember(state, action, reward, next_state, done)

    # Let the agent learn from its experiences if memory is of adequate size
    agent.replay(BATCH_SIZE)

    # Reset the game state if episode is completed
    if done:
        state = get_game_state().state_to_list()