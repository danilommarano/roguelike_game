import pygame
import sys

pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Circle properties
CIRCLE_SPEED = 5

# Bullet properties
BULLET_WIDTH, BULLET_HEIGHT = 8, 20
BULLET_SPEED = 10

class Player:

    radius = 20
    speed = 5
    color = (255, 255, 255)

    bullets = []

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        # Calculate the new position
        keys = pygame.key.get_pressed()
        new_x = self.x
        new_y = self.y
        if keys[pygame.K_w]:
            new_y = self.y - self.speed
        if keys[pygame.K_s]:
            new_y = self.y + self.speed
        if keys[pygame.K_a]:
            new_x = self.x - self.speed
        if keys[pygame.K_d]:
            new_x = self.x + self.speed

        # Check if the new position is within the screen boundaries
        if self.radius <= new_x <= SCREEN_WIDTH - self.radius:
            self.x = new_x
        if self.radius <= new_y <= SCREEN_HEIGHT - self.radius:
            self.y = new_y

    def shoot(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            bullet = Bullet(self.x, self.y, 0, -1)
            self.bullets.append(bullet)

        if keys[pygame.K_DOWN]:
            bullet = Bullet(self.x, self.y, 0, 1)
            self.bullets.append(bullet)

        if keys[pygame.K_LEFT]:
            bullet = Bullet(self.x, self.y, -1, 0)
            self.bullets.append(bullet)
            
        if keys[pygame.K_RIGHT]:
            bullet = Bullet(self.x, self.y, 1, 0)
            self.bullets.append(bullet)
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class Bullet:
    radius = 5
    speed = 10
    color = (255, 0, 0)
    def __init__(self, x, y, dx, dy):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
    
    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

# Initialize the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Move the Circle (WASD) and Shoot (Arrow Keys)")

player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
bullets = []

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Shoot and move
    player.move()
    player.shoot()

    # Clear the screen
    screen.fill(BLACK)

    # Move the bullets
    for bullet in player.bullets:
        bullet.move()

    # Remove the bullets outside of the screen
    player.bullets = [bullet for bullet in player.bullets if (0 <= bullet.x <= SCREEN_WIDTH) and (0 <= bullet.y <= SCREEN_HEIGHT)]

    # Draw player.bullets
    for bullet in player.bullets:
        bullet.draw()

    player.draw()

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
