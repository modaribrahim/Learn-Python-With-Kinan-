# Simple Shooter Game - Learn user input and collision detection
import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Shooter")
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 50
        self.width = 40
        self.height = 30
        self.speed = 5
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)

    def move_left(self):
        self.x = max(self.width//2, self.x - self.speed)
        self.rect.x = self.x - self.width//2

    def move_right(self):
        self.x = min(SCREEN_WIDTH - self.width//2, self.x + self.speed)
        self.rect.x = self.x - self.width//2

    def draw(self, surface):
        pygame.draw.polygon(surface, GREEN, [
            (self.x, self.y - self.height//2),
            (self.x - self.width//2, self.y + self.height//2),
            (self.x + self.width//2, self.y + self.height//2)
        ])

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 8
        self.width = 5
        self.height = 10
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y - self.height//2

    def draw(self, surface):
        pygame.draw.rect(surface, WHITE, self.rect)

    def is_off_screen(self):
        return self.y < 0

class Enemy:
    def __init__(self):
        self.x = random.randint(20, SCREEN_WIDTH - 20)
        self.y = -30
        self.width = 30
        self.height = 30
        self.speed = random.randint(2, 4)
        self.rect = pygame.Rect(self.x - self.width//2, self.y - self.height//2, self.width, self.height)

    def update(self):
        self.y += self.speed
        self.rect.y = self.y - self.height//2

    def draw(self, surface):
        pygame.draw.rect(surface, RED, self.rect)

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

# Game variables
player = Player()
bullets = []
enemies = []
score = 0
game_over = False
enemy_spawn_timer = 0

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullets.append(Bullet(player.x, player.y))

    if not game_over:
        # Handle continuous key input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            player.move_left()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            player.move_right()

        # Spawn enemies
        enemy_spawn_timer += 1
        if enemy_spawn_timer >= 60:  # Spawn every second
            enemies.append(Enemy())
            enemy_spawn_timer = 0

        # Update bullets
        for bullet in bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                bullets.remove(bullet)

        # Update enemies
        for enemy in enemies[:]:
            enemy.update()
            if enemy.is_off_screen():
                enemies.remove(enemy)
                game_over = True

            # Check collision with player
            if player.rect.colliderect(enemy.rect):
                game_over = True

        # Check bullet-enemy collisions
        for bullet in bullets[:]:
            for enemy in enemies[:]:
                if bullet.rect.colliderect(enemy.rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)
                    score += 10
                    break

    # Drawing
    screen.fill(BLACK)

    if not game_over:
        player.draw(screen)
        for bullet in bullets:
            bullet.draw(screen)
        for enemy in enemies:
            enemy.draw(screen)

        # Draw score
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

    else:
        # Game over screen
        font = pygame.font.Font(None, 72)
        game_over_text = font.render("GAME OVER", True, RED)
        score_text = font.render(f"Final Score: {score}", True, WHITE)

        screen.blit(game_over_text, game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50)))
        screen.blit(score_text, score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50)))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()