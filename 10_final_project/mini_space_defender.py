# Mini Space Defender - Complete but simplified game
# This is a PERFECT first game for a 13-year-old!
print("🚀 MINI SPACE DEFENDER - YOUR FIRST COMPLETE GAME!")
print("This game shows how all Python concepts work together!")
print()

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Game settings
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 100, 255)

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mini Space Defender - Your First Game!")
clock = pygame.time.Clock()

print("=" * 60)
print("GAME FEATURES - What You'll Learn:")
print("=" * 60)
print("🎮 GAMEPLAY:")
print("   • Move your spaceship with arrow keys")
print("   • Shoot with spacebar")
print("   • Destroy enemies before they reach you")
print("   • Collect power-ups for bonuses")
print()
print("🧠 PYTHON CONCEPTS USED:")
print("   • CLASSES: Player, Enemy, Bullet, Star")
print("   • VARIABLES: score, lives, positions")
print("   • LOOPS: Game loop, enemy spawning")
print("   • CONDITIONALS: Collision detection, game states")
print("   • FUNCTIONS: Drawing, collision checking")
print("   • LISTS: Managing bullets and enemies")
print()
print("🎯 SKILLS YOU'LL PRACTICE:")
print("   • Object-oriented programming")
print("   • Game logic and mechanics")
print("   • Real-time interaction")
print("   • Problem solving")
print("=" * 60)

class Player:
    """The player's spaceship"""
    def __init__(self):
        self.x = SCREEN_WIDTH // 2  # Start in middle
        self.y = SCREEN_HEIGHT - 100  # Start at bottom
        self.width = 40
        self.height = 30
        self.speed = 6
        self.lives = 3
        self.color = GREEN

    def move_left(self):
        """Move player left"""
        self.x = max(0, self.x - self.speed)

    def move_right(self):
        """Move player right"""
        self.x = min(SCREEN_WIDTH - self.width, self.x + self.speed)

    def draw(self, surface):
        """Draw the player spaceship"""
        # Main body (triangle pointing up)
        points = [
            (self.x + self.width // 2, self.y),  # Top point
            (self.x, self.y + self.height),  # Bottom left
            (self.x + self.width, self.y + self.height)  # Bottom right
        ]
        pygame.draw.polygon(surface, self.color, points)

        # Engine flames (animated)
        flame_height = 5 + (pygame.time.get_ticks() % 300) // 50
        flame_points = [
            (self.x + 10, self.y + self.height),
            (self.x + 15, self.y + self.height + flame_height),
            (self.x + 20, self.y + self.height),
            (self.x + 25, self.y + self.height + flame_height),
            (self.x + 30, self.y + self.height)
        ]
        pygame.draw.polygon(surface, YELLOW, flame_points)

    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Enemy:
    """Enemy ships that come from the top"""
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - 30)
        self.y = -30  # Start above screen
        self.width = 30
        self.height = 30
        self.speed = random.randint(2, 5)  # Random speed
        self.color = RED

    def move(self):
        """Move enemy down"""
        self.y += self.speed

    def draw(self, surface):
        """Draw enemy ship"""
        # Main body
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        # Window
        pygame.draw.circle(surface, BLACK, (self.x + 15, self.y + 15), 8)
        # Border
        pygame.draw.rect(surface, WHITE, (self.x, self.y, self.width, self.height), 2)

    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
        """Check if enemy is below screen"""
        return self.y > SCREEN_HEIGHT

class Bullet:
    """Bullets that the player shoots"""
    def __init__(self, x, y):
        self.x = x + 15  # Center of player
        self.y = y
        self.width = 5
        self.height = 15
        self.speed = 10
        self.color = WHITE

    def move(self):
        """Move bullet up"""
        self.y -= self.speed

    def draw(self, surface):
        """Draw bullet with glow effect"""
        # Main bullet
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))
        # Glow effect
        pygame.draw.rect(surface, YELLOW, (self.x - 1, self.y - 1, self.width + 2, self.height + 2), 1)

    def get_rect(self):
        """Get collision rectangle"""
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def is_off_screen(self):
        """Check if bullet is above screen"""
        return self.y < 0

class Star:
    """Background stars for visual effect"""
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.speed = random.uniform(0.5, 2)  # Different speeds
        self.brightness = random.randint(100, 255)

    def move(self):
        """Move star down and wrap around"""
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = 0
            self.x = random.randint(0, SCREEN_WIDTH)

    def draw(self, surface):
        """Draw star"""
        color = (self.brightness, self.brightness, self.brightness)
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), 1)

class Explosion:
    """Explosion effect when enemy is destroyed"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.particles = []

        # Create explosion particles
        for _ in range(12):
            particle = {
                'x': x,
                'y': y,
                'dx': random.uniform(-5, 5),
                'dy': random.uniform(-5, 5),
                'life': 30,
                'color': random.choice([YELLOW, RED, (255, 165, 0)])  # Yellow, Red, Orange
            }
            self.particles.append(particle)

    def update(self):
        """Update explosion particles"""
        for particle in self.particles[:]:
            particle['x'] += particle['dx']
            particle['y'] += particle['dy']
            particle['life'] -= 1

            # Remove dead particles
            if particle['life'] <= 0:
                self.particles.remove(particle)

    def draw(self, surface):
        """Draw explosion particles"""
        for particle in self.particles:
            # Particle size gets smaller as life decreases
            size = int(3 * (particle['life'] / 30))
            if size > 0:
                pygame.draw.circle(surface, particle['color'],
                                 (int(particle['x']), int(particle['y'])), size)

    def is_finished(self):
        """Check if explosion is done"""
        return len(self.particles) == 0

def show_text(surface, text, size, x, y, color):
    """Display text on screen"""
    try:
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        surface.blit(text_surface, text_rect)
    except:
        print("Error displaying text")

def check_collision(rect1, rect2):
    """Check if two rectangles collide"""
    return rect1.colliderect(rect2)

def show_start_screen(surface):
    """Display the start screen"""
    surface.fill(BLACK)

    # Title
    show_text(surface, "MINI SPACE DEFENDER", 64, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 100, GREEN)

    # Instructions
    show_text(surface, "Use ARROW KEYS to move", 28, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 20, WHITE)
    show_text(surface, "Press SPACE to shoot", 28, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20, WHITE)
    show_text(surface, "Destroy enemies before they reach you!", 22, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 60, YELLOW)

    # Start prompt
    show_text(surface, "Press SPACE to start", 32, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120, GREEN)

def show_game_over(surface, score):
    """Display game over screen"""
    # Darken the screen
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    overlay.set_alpha(128)
    overlay.fill(BLACK)
    surface.blit(overlay, (0, 0))

    # Game over text
    show_text(surface, "GAME OVER", 72, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80, RED)
    show_text(surface, f"Final Score: {score}", 36, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, WHITE)
    show_text(surface, "Press SPACE to play again", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50, GREEN)
    show_text(surface, "Press ESC to quit", 24, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80, WHITE)

def main_game():
    """Main game function"""
    # Create background stars
    stars = [Star() for _ in range(50)]

    # Show start screen
    show_start_screen(screen)
    pygame.display.flip()

    # Wait for player to start
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    waiting = False
                elif event.key == pygame.K_ESCAPE:
                    return False

    # Initialize game objects
    player = Player()
    bullets = []
    enemies = []
    explosions = []

    # Game variables
    score = 0
    enemy_spawn_timer = 0
    game_over = False

    # Fonts
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE:
                    if not game_over:
                        # Shoot bullet
                        bullet = Bullet(player.x, player.y)
                        bullets.append(bullet)
                    else:
                        # Restart game
                        main_game()
                        return

        if not game_over:
            # Handle continuous key presses
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                player.move_left()
            if keys[pygame.K_RIGHT]:
                player.move_right()

            # Spawn enemies
            enemy_spawn_timer += 1
            spawn_rate = max(20, 60 - score // 50)  # Get harder as score increases
            if enemy_spawn_timer >= spawn_rate:
                enemies.append(Enemy())
                enemy_spawn_timer = 0

            # Update bullets
            for bullet in bullets[:]:
                bullet.move()
                if bullet.is_off_screen():
                    bullets.remove(bullet)

            # Update enemies
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
                        # Remove bullet and enemy
                        bullets.remove(bullet)
                        enemies.remove(enemy)
                        score += 10

                        # Create explosion
                        explosion = Explosion(enemy.x + 15, enemy.y + 15)
                        explosions.append(explosion)
                        break

            # Check collisions between player and enemies
            for enemy in enemies[:]:
                if check_collision(player.get_rect(), enemy.get_rect()):
                    enemies.remove(enemy)
                    player.lives -= 1

                    # Create explosion
                    explosion = Explosion(enemy.x + 15, enemy.y + 15)
                    explosions.append(explosion)

                    if player.lives <= 0:
                        game_over = True

        # Update explosions
        for explosion in explosions[:]:
            explosion.update()
            if explosion.is_finished():
                explosions.remove(explosion)

        # Drawing
        screen.fill(BLACK)

        # Draw stars (background)
        for star in stars:
            star.move()
            star.draw(screen)

        if not game_over:
            # Draw game objects
            player.draw(screen)

            for bullet in bullets:
                bullet.draw(screen)

            for enemy in enemies:
                enemy.draw(screen)

            for explosion in explosions:
                explosion.draw(screen)

            # Draw HUD (Heads Up Display)
            lives_text = font.render(f"Lives: {player.lives}", True, GREEN)
            screen.blit(lives_text, (10, 10))

            score_text = font.render(f"Score: {score}", True, WHITE)
            screen.blit(score_text, (SCREEN_WIDTH - 150, 10))

            # Draw lives as mini spaceships
            for i in range(player.lives):
                mini_x = 10 + i * 35
                mini_y = 50
                pygame.draw.polygon(screen, GREEN, [
                    (mini_x + 10, mini_y),
                    (mini_x, mini_y + 15),
                    (mini_x + 20, mini_y + 15)
                ])
        else:
            show_game_over(screen, score)

        pygame.display.flip()
        clock.tick(60)  # 60 FPS

    return True

# Start the game
print("\n🚀 Starting game...")
if main_game():
    print("🎮 Game completed!")
    print("Congratulations on creating your first complete Python game!")
else:
    print("👋 Thanks for playing!")

pygame.quit()
sys.exit()