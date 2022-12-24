import pygame
import random

# Initialize the Pygame library
pygame.init()

# Set the window size and title
window_size = (400, 400)
window_title = "Snake"
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption(window_title)

# Set the block size and margin
block_size = 20
margin = 1

# Set the grid size
grid_width = window_size[0] // block_size
grid_height = window_size[1] // block_size

# Set the initial position of the snake
snake_x = grid_width // 2
snake_y = grid_height // 2
snake_body = [(snake_x, snake_y)]

# Set the initial position of the food
food_x = random.randint(0, grid_width - 1)
food_y = random.randint(0, grid_height - 1)

# Set the initial direction of the snake
direction = "UP"

# Set the frame rate
frame_rate = 10
clock = pygame.time.Clock()

# Set the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set the game over flag
game_over = False

# Function to draw the snake
def draw_snake():
    for x, y in snake_body:
        pygame.draw.rect(screen, WHITE, (x * block_size + margin, y * block_size + margin, block_size - 2 * margin, block_size - 2 * margin))

# Function to move the snake
def move_snake():
    global snake_x, snake_y, direction, snake_body, game_over
    if direction == "UP":
        snake_y -= 1
    elif direction == "DOWN":
        snake_y += 1
    elif direction == "LEFT":
        snake_x -= 1
    elif direction == "RIGHT":
        snake_x += 1
    else:
        game_over = True
    snake_body.insert(0, (snake_x, snake_y))
    if snake_x < 0 or snake_x >= grid_width or snake_y < 0 or snake_y >= grid_height:
        game_over = True
    if (snake_x, snake_y) in snake_body[1:]:
        game_over = True
    if snake_x == food_x and snake_y == food_y:
        food_x = random.randint(0, grid_width - 1)
        food_y = random.randint(0, grid_height - 1)
    else:
        snake_body.pop()

# Main game loop
while not game_over:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "UP"
            # elif event.key == pygame.K_DOWN:
