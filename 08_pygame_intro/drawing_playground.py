# Drawing Playground - Learn Pygame drawing and animation
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Drawing Playground")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
ORANGE = (255, 165, 0)

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Random shapes for animation
shapes = []

# Create some random shapes
for _ in range(10):
    shape = {
        'type': random.choice(['rect', 'circle', 'triangle']),
        'x': random.randint(50, SCREEN_WIDTH - 50),
        'y': random.randint(50, SCREEN_HEIGHT - 50),
        'size': random.randint(20, 60),
        'color': random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, ORANGE]),
        'speed': random.uniform(1, 3),
        'direction': random.uniform(0, 2 * 3.14159)  # Random angle
    }
    shapes.append(shape)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Add new shape at mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            new_shape = {
                'type': random.choice(['rect', 'circle', 'triangle']),
                'x': mouse_x,
                'y': mouse_y,
                'size': random.randint(20, 60),
                'color': random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, CYAN, ORANGE]),
                'speed': random.uniform(1, 3),
                'direction': random.uniform(0, 2 * 3.14159)
            }
            shapes.append(new_shape)

    # Clear screen
    screen.fill(BLACK)

    # Update and draw shapes
    for shape in shapes[:]:
        # Update position
        shape['x'] += shape['speed'] * (shape['direction'] % 1)
        shape['y'] += shape['speed'] * ((shape['direction'] + 1) % 1)

        # Bounce off walls
        if shape['x'] <= shape['size'] or shape['x'] >= SCREEN_WIDTH - shape['size']:
            shape['direction'] = 3.14159 - shape['direction']
        if shape['y'] <= shape['size'] or shape['y'] >= SCREEN_HEIGHT - shape['size']:
            shape['direction'] = -shape['direction']

        # Draw shape
        if shape['type'] == 'rect':
            pygame.draw.rect(screen, shape['color'],
                           (shape['x'] - shape['size'], shape['y'] - shape['size'],
                            shape['size'] * 2, shape['size'] * 2))
        elif shape['type'] == 'circle':
            pygame.draw.circle(screen, shape['color'],
                             (int(shape['x']), int(shape['y'])), shape['size'])
        elif shape['type'] == 'triangle':
            points = [
                (shape['x'], shape['y'] - shape['size']),
                (shape['x'] - shape['size'], shape['y'] + shape['size']),
                (shape['x'] + shape['size'], shape['y'] + shape['size'])
            ]
            pygame.draw.polygon(screen, shape['color'], points)

    # Draw some static shapes for reference
    font = pygame.font.Font(None, 24)

    # Instructions
    text = font.render("Click to add shapes!", True, WHITE)
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30))
    screen.blit(text, text_rect)

    # Update display
    pygame.display.flip()
    clock.tick(60)  # 60 FPS

# Quit
pygame.quit()
sys.exit()