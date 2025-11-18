# Collision Detection Demo - Learn how objects interact!
print("💥 COLLISION DETECTION DEMO - LEARN GAME MECHANICS!")
print("This teaches you how to know when objects touch in games!")
print()

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision Detection Demo")
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)

class Player:
    """Player that you can move with arrow keys"""
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT // 2
        self.size = 30
        self.speed = 5
        self.color = GREEN
        self.score = 0

    def move(self, keys):
        """Move player based on arrow keys"""
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x = max(self.size, self.x - self.speed)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x = min(SCREEN_WIDTH - self.size, self.x + self.speed)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y = max(self.size, self.y - self.speed)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y = min(SCREEN_HEIGHT - self.size, self.y + self.speed)

    def get_rect(self):
        """Get the rectangle for collision detection"""
        return pygame.Rect(self.x - self.size, self.y - self.size,
                          self.size * 2, self.size * 2)

    def draw(self, surface):
        """Draw the player"""
        # Draw main circle
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.size)
        # Draw border
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), self.size, 2)

class Collectible:
    """Item that player can collect"""
    def __init__(self):
        self.reset_position()
        self.size = 20
        self.color = YELLOW
        self.pulse = 0  # For pulsing animation

    def reset_position(self):
        """Move to random position"""
        self.x = random.randint(50, SCREEN_WIDTH - 50)
        self.y = random.randint(50, SCREEN_HEIGHT - 50)

    def get_rect(self):
        """Get the rectangle for collision detection"""
        return pygame.Rect(self.x - self.size, self.y - self.size,
                          self.size * 2, self.size * 2)

    def update(self):
        """Update animation"""
        self.pulse += 0.1

    def draw(self, surface):
        """Draw with pulsing effect"""
        # Pulsing size
        current_size = self.size + int(3 * abs(self.sin(self.pulse)))
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), current_size)
        pygame.draw.circle(surface, WHITE, (int(self.x), int(self.y)), current_size, 2)

    def sin(self, x):
        """Simple sine function for pulsing"""
        # Approximation of sin(x)
        return x * (3.14159 - abs(x % (2 * 3.14159) - 3.14159)) / (3.14159 * 3.14159)

class Enemy:
    """Simple enemy that moves randomly"""
    def __init__(self):
        self.x = random.randint(50, SCREEN_WIDTH - 50)
        self.y = random.randint(50, SCREEN_HEIGHT - 50)
        self.size = 25
        self.speed = 2
        self.color = RED
        self.direction = random.uniform(0, 2 * 3.14159)  # Random angle

    def get_rect(self):
        """Get the rectangle for collision detection"""
        return pygame.Rect(self.x - self.size, self.y - self.size,
                          self.size * 2, self.size * 2)

    def update(self):
        """Move enemy in random direction"""
        # Move in current direction
        self.x += self.speed * self.cos(self.direction)
        self.y += self.speed * self.sin(self.direction)

        # Bounce off walls
        if self.x <= self.size or self.x >= SCREEN_WIDTH - self.size:
            self.direction = 3.14159 - self.direction
        if self.y <= self.size or self.y >= SCREEN_HEIGHT - self.size:
            self.direction = -self.direction

        # Randomly change direction sometimes
        if random.random() < 0.02:  # 2% chance
            self.direction += random.uniform(-0.5, 0.5)

    def cos(self, x):
        """Simple cosine function"""
        return self.sin(x + 1.5708)

    def sin(self, x):
        """Simple sine function"""
        return x * (3.14159 - abs(x % (2 * 3.14159) - 3.14159)) / (3.14159 * 3.14159)

    def draw(self, surface):
        """Draw the enemy"""
        # Draw square enemy
        rect = pygame.Rect(self.x - self.size, self.y - self.size,
                          self.size * 2, self.size * 2)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, WHITE, rect, 2)

def check_collision(rect1, rect2):
    """
    Check if two rectangles are colliding (overlapping)
    This is the most important function in game mechanics!
    """
    return rect1.colliderect(rect2)

def check_circle_collision(obj1, obj2):
    """
    Check if two circles are colliding
    Alternative method for circular objects
    """
    # Calculate distance between centers
    distance = ((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) ** 0.5
    # Check if distance is less than sum of radii
    return distance < (obj1.size + obj2.size)

print("=" * 60)
print("COLLISION DETECTION EXPLANATION:")
print("=" * 60)
print("🎮 What is Collision Detection?")
print("   It's how games know when objects touch each other!")
print()
print("💡 Why is it important?")
print("   - Bullets hitting enemies")
print("   - Player collecting items")
print("   - Player avoiding obstacles")
print("   - Cars crashing in racing games")
print()
print("🔧 How does it work?")
print("   - Rectangle collision: Check if rectangles overlap")
print("   - Circle collision: Check distance between centers")
print("   - Point collision: Check if point is inside shape")
print()
print("🎯 In this demo you'll see:")
print("   - GREEN circle: Your player (use arrow keys to move)")
print("   - YELLOW circles: Collectible items (+10 points)")
print("   - RED squares: Avoid these enemies (-20 points)")
print("   - Watch for collision messages!")
print("=" * 60)

# Create game objects
player = Player()
collectibles = [Collectible() for _ in range(3)]
enemies = [Enemy() for _ in range(2)]

# Game variables
running = True
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)
collision_messages = []  # Store collision messages to display

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_SPACE:
                # Reset game
                player.score = 0
                player.x = SCREEN_WIDTH // 2
                player.y = SCREEN_HEIGHT // 2
                for collectible in collectibles:
                    collectible.reset_position()
                for enemy in enemies:
                    enemy.x = random.randint(50, SCREEN_WIDTH - 50)
                    enemy.y = random.randint(50, SCREEN_HEIGHT - 50)
                collision_messages.clear()
                collision_messages.append("Game Reset!")

    # Get keyboard input
    keys = pygame.key.get_pressed()

    # Update player
    player.move(keys)

    # Update collectibles
    for collectible in collectibles:
        collectible.update()

    # Update enemies
    for enemy in enemies:
        enemy.update()

    # Check collisions - THIS IS THE IMPORTANT PART!
    for collectible in collectibles:
        # Check if player touched a collectible
        if check_collision(player.get_rect(), collectible.get_rect()):
            # Alternative: if check_circle_collision(player, collectible):
            player.score += 10
            collectible.reset_position()
            collision_messages.append(f"💰 Collected! +10 points (Score: {player.score})")

    for enemy in enemies:
        # Check if player touched an enemy
        if check_collision(player.get_rect(), enemy.get_rect()):
            player.score = max(0, player.score - 20)
            enemy.x = random.randint(50, SCREEN_WIDTH - 50)
            enemy.y = random.randint(50, SCREEN_HEIGHT - 50)
            collision_messages.append(f"💀 Hit enemy! -20 points (Score: {player.score})")

    # Update collision messages (remove old ones)
    collision_messages = collision_messages[-3:]  # Keep only last 3 messages

    # Drawing
    screen.fill(BLACK)

    # Draw game objects
    player.draw(screen)

    for collectible in collectibles:
        collectible.draw(screen)

    for enemy in enemies:
        enemy.draw(screen)

    # Draw UI
    score_text = font.render(f"Score: {player.score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # Draw collision detection status
    player_rect = player.get_rect()
    status_text = small_font.render(f"Player position: ({int(player.x)}, {int(player.y)})", True, WHITE)
    screen.blit(status_text, (10, 50))

    # Show collision areas (for learning)
    pygame.draw.rect(screen, (0, 255, 0, 50), player_rect, 2)  # Green outline around player

    # Draw collision messages
    y_offset = SCREEN_HEIGHT - 100
    for message in collision_messages:
        msg_text = small_font.render(message, True, YELLOW)
        screen.blit(msg_text, (10, y_offset))
        y_offset += 25

    # Draw instructions
    instructions = [
        "Arrow Keys/WASD: Move",
        "SPACE: Reset game",
        "ESC: Quit",
        "Watch for collision messages!"
    ]

    y_offset = 100
    for instruction in instructions:
        inst_text = small_font.render(instruction, True, WHITE)
        screen.blit(inst_text, (SCREEN_WIDTH - 250, y_offset))
        y_offset += 25

    # Update display
    pygame.display.flip()
    clock.tick(60)

# Clean up
pygame.quit()
sys.exit()

print("\n🎉 Congratulations!")
print("You've learned how collision detection works in games!")
print("\nKey concepts you now understand:")
print("✅ Rectangle collision detection")
print("✅ Circle collision detection")
print("✅ Real-time collision checking")
print("✅ Game responses to collisions")
print("✅ Visual feedback for collisions")
print("\nYou can now add collision detection to your own games!")