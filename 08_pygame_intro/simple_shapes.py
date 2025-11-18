# Simple Pygame Shapes - Learn the basics!
# This file teaches Pygame step by step!

import pygame
import sys
import random

print("🎮 SIMPLE PYGAME SHAPES - STEP BY STEP!")
print("This will teach you Pygame basics with clear explanations!")
print()

# STEP 1: Initialize Pygame
print("Step 1: Starting Pygame...")
pygame.init()
print("✅ Pygame started!")

# STEP 2: Set up the screen
print("Step 2: Creating game window...")
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Learn Pygame - Simple Shapes")
print("✅ Window created!")

# STEP 3: Define colors (RGB format)
print("Step 3: Setting up colors...")
# Colors are made of Red, Green, Blue values (0-255)
BLACK = (0, 0, 0)        # No color
WHITE = (255, 255, 255)  # All colors
RED = (255, 0, 0)        # Only red
GREEN = (0, 255, 0)      # Only green
BLUE = (0, 0, 255)       # Only blue
YELLOW = (255, 255, 0)   # Red + Green
PURPLE = (255, 0, 255)   # Red + Blue
CYAN = (0, 255, 255)     # Green + Blue
ORANGE = (255, 165, 0)   # Custom color
print("✅ Colors ready!")

# STEP 4: Set up the clock for controlling speed
clock = pygame.time.Clock()
print("✅ Clock ready!")

# STEP 5: Game variables
print("Step 5: Setting up game variables...")
running = True
background_color = BLACK
current_shape = "rectangle"
shape_x = 400
shape_y = 300
shape_size = 50
move_speed = 5

# Create some bouncing balls for animation
balls = []
for i in range(3):
    ball = {
        'x': random.randint(50, SCREEN_WIDTH - 50),
        'y': random.randint(50, SCREEN_HEIGHT - 50),
        'dx': random.randint(3, 8),  # Horizontal speed
        'dy': random.randint(3, 8),  # Vertical speed
        'color': random.choice([RED, GREEN, BLUE, YELLOW, PURPLE, CYAN]),
        'size': random.randint(20, 40)
    }
    balls.append(ball)

print(f"✅ Created {len(balls)} bouncing balls!")

print("\n" + "=" * 50)
print("GAME INSTRUCTIONS:")
print("=" * 50)
print("🎮 CONTROLS:")
print("  Arrow Keys: Move the main shape")
print("  1: Rectangle  | 2: Circle  | 3: Triangle")
print("  R: Red  | G: Green  | B: Blue  | Y: Yellow")
print("  SPACE: Change background color")
print("  C: Clear screen  | ESC: Quit game")
print()
print("🎯 WHAT YOU'LL SEE:")
print("  - A shape you can control with arrow keys")
print("  - Bouncing balls that demonstrate animation")
print("  - Color changing to show how Pygame works")
print("  - Real-time drawing and movement")
print("=" * 50)

# STEP 6: Main game loop
print("\n🚀 Starting game loop...")

while running:
    # Handle events (keyboard, mouse, window close)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Window closed - quitting game...")
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("ESC pressed - quitting game...")
                running = False

            # Change shapes
            elif event.key == pygame.K_1:
                current_shape = "rectangle"
                print("Changed to Rectangle")
            elif event.key == pygame.K_2:
                current_shape = "circle"
                print("Changed to Circle")
            elif event.key == pygame.K_3:
                current_shape = "triangle"
                print("Changed to Triangle")

            # Change colors
            elif event.key == pygame.K_r:
                shape_color = RED
                print("Changed to Red")
            elif event.key == pygame.K_g:
                shape_color = GREEN
                print("Changed to Green")
            elif event.key == pygame.K_b:
                shape_color = BLUE
                print("Changed to Blue")
            elif event.key == pygame.K_y:
                shape_color = YELLOW
                print("Changed to Yellow")

            # Change background
            elif event.key == pygame.K_SPACE:
                colors = [BLACK, (20, 20, 40), (40, 0, 40), (0, 40, 40)]
                background_color = random.choice(colors)
                print(f"Background changed to {background_color}")

            # Clear screen
            elif event.key == pygame.K_c:
                balls.clear()
                print("Cleared all bouncing balls")

    # Get current keyboard state (for continuous movement)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        shape_x = max(shape_size, shape_x - move_speed)
    if keys[pygame.K_RIGHT]:
        shape_x = min(SCREEN_WIDTH - shape_size, shape_x + move_speed)
    if keys[pygame.K_UP]:
        shape_y = max(shape_size, shape_y - move_speed)
    if keys[pygame.K_DOWN]:
        shape_y = min(SCREEN_HEIGHT - shape_size, shape_y + move_speed)

    # Update bouncing balls
    for ball in balls[:]:
        # Move ball
        ball['x'] += ball['dx']
        ball['y'] += ball['dy']

        # Bounce off walls (collision detection!)
        if ball['x'] <= ball['size'] or ball['x'] >= SCREEN_WIDTH - ball['size']:
            ball['dx'] = -ball['dx']  # Reverse horizontal direction
            print(f"Ball bounced off vertical wall at x={ball['x']}")

        if ball['y'] <= ball['size'] or ball['y'] >= SCREEN_HEIGHT - ball['size']:
            ball['dy'] = -ball['dy']  # Reverse vertical direction
            print(f"Ball bounced off horizontal wall at y={ball['y']}")

    # STEP 7: Drawing (clear screen, draw everything, update display)
    screen.fill(background_color)

    # Draw bouncing balls
    for ball in balls:
        pygame.draw.circle(screen, ball['color'],
                         (int(ball['x']), int(ball['y'])),
                         ball['size'])
        # Add a white outline
        pygame.draw.circle(screen, WHITE,
                         (int(ball['x']), int(ball['y'])),
                         ball['size'], 2)

    # Draw main shape based on current selection
    shape_color = WHITE

    if current_shape == "rectangle":
        pygame.draw.rect(screen, shape_color,
                        (shape_x - shape_size, shape_y - shape_size,
                         shape_size * 2, shape_size * 2))
        print(f"Drawing rectangle at ({shape_x}, {shape_y})")

    elif current_shape == "circle":
        pygame.draw.circle(screen, shape_color,
                         (shape_x, shape_y), shape_size)
        print(f"Drawing circle at ({shape_x}, {shape_y})")

    elif current_shape == "triangle":
        points = [
            (shape_x, shape_y - shape_size),  # Top point
            (shape_x - shape_size, shape_y + shape_size),  # Bottom left
            (shape_x + shape_size, shape_y + shape_size)   # Bottom right
        ]
        pygame.draw.polygon(screen, shape_color, points)
        print(f"Drawing triangle at ({shape_x}, {shape_y})")

    # Draw instructions on screen
    font = pygame.font.Font(None, 24)
    instructions = [
        "Arrow Keys: Move | 1-3: Change Shape | R/G/B/Y: Colors",
        "SPACE: Background | C: Clear | ESC: Quit"
    ]

    y_offset = 10
    for instruction in instructions:
        text = font.render(instruction, True, WHITE)
        screen.blit(text, (10, y_offset))
        y_offset += 25

    # Draw current info
    info_text = font.render(f"Shape: {current_shape} | Position: ({shape_x}, {shape_y})", True, WHITE)
    screen.blit(info_text, (SCREEN_WIDTH - 400, 10))

    # STEP 8: Update the display
    pygame.display.flip()

    # Control the frame rate (60 FPS = 60 frames per second)
    clock.tick(60)

# STEP 9: Clean up
print("\n🎮 Game ended!")
print("🎉 Congratulations! You've learned the basics of Pygame!")
print("\nWhat you learned:")
print("✅ How to set up a Pygame window")
print("✅ How to draw different shapes")
print("✅ How to handle keyboard input")
print("✅ How to create animations")
print("✅ How to detect collisions (bouncing)")
print("✅ How to control game speed")
print("\nYou're ready to create your own games now!")

pygame.quit()
sys.exit()