"""
SPACE DEFENDER - Complete Python Game
Created by: Kinan (and you!)
This game demonstrates all Python concepts learned in this course
"""

import pygame
import sys
import random
from pygame.locals import *
import math
# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

class Player:
    """Player spaceship class - demonstrates OOP and variables"""
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 50
        self.width = 40
        self.height = 30
        self.speed = 5
        self.lives = 3
        self.score = 0
        self.color = GREEN

    def move_left(self):
        """Move player left - uses conditional logic"""
        self.x = max(0, self.x - self.speed)

    def move_right(self):
        """Move player right - uses conditional logic"""
        self.x = min(SCREEN_WIDTH - self.width, self.x + self.speed)

    def draw(self, surface):
        """Draw the player - demonstrates Pygame graphics"""
        # Draw a triangle spaceship
        points = [
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height)
        ]
        pygame.draw.polygon(surface, self.color, points)

        # Draw engine flame
        flame_points = [
            (self.x + 10, self.y + self.height),
            (self.x + 15, self.y + self.height + 5),
            (self.x + 20, self.y + self.height),
            (self.x + 25, self.y + self.height + 5),
            (self.x + 30, self.y + self.height)
        ]
        pygame.draw.polygon(surface, YELLOW, flame_points)

    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Enemy:
    """Enemy class - demonstrates OOP and random behavior"""
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - 30)
        self.y = -30
        self.width = 30
        self.height = 30
        self.speed = random.randint(2, 4)
        self.color = RED
        self.wobble = random.randint(0, 20)
        self.wobble_speed = random.uniform(0.1, 0.3)

    def move(self):
        """Move enemy down with wobbling motion"""
        self.y += self.speed
        self.wobble += self.wobble_speed
        self.x += math.sin(self.wobble) * 2

    def draw(self, surface):
        """Draw enemy ship"""
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        # Draw enemy details
        pygame.draw.circle(surface, BLACK, (self.x + 15, self.y + 15), 5)

    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
        """Check if enemy is off screen - demonstrates conditionals"""
        return self.y > SCREEN_HEIGHT

class Bullet:
    """Bullet class - demonstrates OOP and physics"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 5
        self.height = 10
        self.speed = 7
        self.color = WHITE

    def move(self):
        """Move bullet up"""
        self.y -= self.speed

    def draw(self, surface):
        """Draw bullet with glow effect"""
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        # Add glow
        pygame.draw.rect(surface, YELLOW, (self.x-1, self.y-1, self.width+2, self.height+2), 1)

    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
        """Check if bullet is off screen"""
        return self.y < 0

class Star:
    """Background star class for visual effects"""
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.speed = random.uniform(0.5, 2)
        self.brightness = random.randint(100, 255)

    def move(self):
        """Move star down"""
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, surface):
        """Draw star"""
        color = (self.brightness, self.brightness, self.brightness)
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 1)

# Game Functions - demonstrate function organization

def show_text(surface, text, size, x, y, color):
    """Display text on screen - demonstrates function parameters and returns"""
    try:
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, text_rect)
    except:
        print("Error displaying text")

def check_collision(rect1, rect2):
    """Check if two rectangles collide - demonstrates conditional logic"""
    return rect1.colliderect(rect2)

def show_game_over(surface, score):
    """Display game over screen - demonstrates complex functions"""
    # Create semi-transparent overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    surface.blit(overlay, (0, 0))

    # Show game over text
    show_text(surface, "GAME OVER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50, RED)
    show_text(surface, f"Final Score: {score}", 36, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, WHITE)
    show_text(surface, "Press SPACE to play again", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80, GREEN)
    show_text(surface, "Press ESC to quit", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 110, WHITE)

def show_start_screen(surface):
    """Display start screen - demonstrates function composition"""
    surface.fill(BLACK)

    # Title
    show_text(surface, "SPACE DEFENDER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, GREEN)

    # Instructions
    show_text(surface, "Use ARROW KEYS to move", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, WHITE)
    show_text(surface, "Press SPACE to shoot", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 10, WHITE)
    show_text(surface, "Destroy enemies before they reach you!", 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40, YELLOW)

    # Start prompt
    show_text(surface, "Press SPACE to start", 36, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100, GREEN)

def create_explosion_particles(x, y):
    """Create explosion effect - demonstrates list generation"""
    particles = []
    for _ in range(10):
        particle = {
            'x': x,
            'y': y,
            'vx': random.uniform(-3, 3),
            'vy': random.uniform(-3, 3),
            'life': 30
        }
        particles.append(particle)
    return particles

def update_and_draw_particles(surface, particles):
    """Update and draw particle effects"""
    for particle in particles[:]:
        particle['x'] += particle['vx']
        particle['y'] += particle['vy']
        particle['life'] -= 1

        if particle['life'] <= 0:
            particles.remove(particle)
        else:
            alpha = particle['life'] / 30
            size = int(3 * alpha)
            color = (255, int(200 * alpha), 0)
            pygame.draw.circle(surface, color, (int(particle['x']), int(particle['y'])), size)

def main():
    """Main game function - demonstrates program structure and game loops"""
    # Import math here to avoid potential circular import
    import math

    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Defender - Your First Python Game!")
    clock = pygame.time.Clock()

    # Create background stars
    stars = [Star() for _ in range(50)]

    # Show start screen
    show_start_screen(screen)
    pygame.display.flip()

    # Wait for player to start
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    waiting = False
                elif event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    # Initialize game objects
    player = Player()
    enemies = []
    bullets = []
    particles = []
    enemy_spawn_timer = 0
    game_over = False

    # Game fonts
    font = pygame.font.Font(None, 36)
    big_font = pygame.font.Font(None, 72)

    # Main game loop - demonstrates loops and event handling
    running = True
    while running:
        # Handle events - demonstrates conditional logic
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE and not game_over:
                    # Shoot bullet
                    bullet = Bullet(player.x + player.width // 2 - 2, player.y)
                    bullets.append(bullet)
                elif event.key == K_SPACE and game_over:
                    # Restart game - demonstrates recursion
                    main()
                    return

        if not game_over:
            # Handle continuous key presses
            keys = pygame.key.get_pressed()
            if keys[K_LEFT]:
                player.move_left()
            if keys[K_RIGHT]:
                player.move_right()

            # Spawn enemies - demonstrates timers and conditionals
            enemy_spawn_timer += 1
            spawn_rate = max(30, 60 - player.score // 100)  # Increase difficulty
            if enemy_spawn_timer >= spawn_rate:
                enemies.append(Enemy())
                enemy_spawn_timer = 0

            # Update bullets - demonstrates list manipulation
            for bullet in bullets[:]:
                bullet.move()
                if bullet.is_off_screen():
                    bullets.remove(bullet)

            # Update enemies - demonstrates loops and conditional logic
            for enemy in enemies[:]:
                enemy.move()
                if enemy.is_off_screen():
                    enemies.remove(enemy)
                    player.lives -= 1
                    if player.lives <= 0:
                        game_over = True

            # Check collisions between bullets and enemies
            for bullet in bullets[:]:
                for enemy in enemies[:]:
                    if check_collision(bullet.get_rect(), enemy.get_rect()):
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        player.score += 10

                        # Create explosion effect
                        explosion_particles = create_explosion_particles(enemy.x + 15, enemy.y + 15)
                        particles.extend(explosion_particles)
                        break

            # Check collisions between player and enemies
            for enemy in enemies[:]:
                if check_collision(player.get_rect(), enemy.get_rect()):
                    enemies.remove(enemy)
                    player.lives -= 1

                    # Create explosion effect
                    explosion_particles = create_explosion_particles(enemy.x + 15, enemy.y + 15)
                    particles.extend(explosion_particles)

                    if player.lives <= 0:
                        game_over = True

        # Drawing - demonstrates Pygame graphics
        screen.fill(BLACK)

        # Draw stars (background)
        for star in stars:
            star.move()
            star.draw(screen)

        if not game_over:
            # Draw game objects
            player.draw(screen)

            for enemy in enemies:
                enemy.draw(screen)

            for bullet in bullets:
                bullet.draw(screen)

            # Draw particle effects
            update_and_draw_particles(screen, particles)

            # Draw HUD (Heads Up Display)
            lives_text = font.render(f"Lives: {player.lives}", True, GREEN)
            screen.blit(lives_text, (10, 10))

            score_text = font.render(f"Score: {player.score}", True, WHITE)
            screen.blit(score_text, (SCREEN_WIDTH - 150, 10))

            # Draw lives as little ships
            for i in range(player.lives):
                mini_ship_x = 10 + i * 35
                mini_ship_y = 50
                pygame.draw.polygon(screen, GREEN, [
                    (mini_ship_x + 10, mini_ship_y),
                    (mini_ship_x, mini_ship_y + 15),
                    (mini_ship_x + 20, mini_ship_y + 15)
                ])

        else:
            # Game over screen
            show_game_over(screen, player.score)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    pygame.quit()
    sys.exit()

# Entry point - demonstrates Python program structure
if __name__ == "__main__":
    main()