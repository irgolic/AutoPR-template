import pygame
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define game paddles and ball
LEFT_PADDLE = pygame.Rect(20, 20, 10, 100)
RIGHT_PADDLE = pygame.Rect(SCREEN_WIDTH - 30, 20, 10, 100)
BALL = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 15, 15)

# Game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Colors
WHITE = (255, 255, 255)

# Game loop
running = True
while running:
    # Handle user events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    
    # Update game logic
    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        LEFT_PADDLE.move_ip(0, -5)
    if keys[K_s]:
        LEFT_PADDLE.move_ip(0, 5)
    if keys[K_UP]:
        RIGHT_PADDLE.move_ip(0, -5)
    if keys[K_DOWN]:
        RIGHT_PADDLE.move_ip(0, 5)

    # Collision detection
    LEFT_PADDLE.clamp_ip(screen.get_rect())
    RIGHT_PADDLE.clamp_ip(screen.get_rect())

    # Ball movement
    BALL.move_ip(2, 2)
    if BALL.colliderect(LEFT_PADDLE) or BALL.colliderect(RIGHT_PADDLE):
        BALL.x *= -1
    if BALL.y <= 0 or BALL.y >= SCREEN_HEIGHT - 15:
        BALL.y *= -1

    # Redraw game objects
    screen.fill(0)
    pygame.draw.rect(screen, WHITE, LEFT_PADDLE)
    pygame.draw.rect(screen, WHITE, RIGHT_PADDLE)
    pygame.draw.rect(screen, WHITE, BALL)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()