import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Color Change Example")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define custom event for changing sprite color
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1

# Create a simple sprite class
class MySprite(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def change_color(self, new_color):
        self.image.fill(new_color)

# Create two sprite objects
sprite1 = MySprite(RED, WIDTH // 3, HEIGHT // 2)
sprite2 = MySprite(GREEN, 2 * WIDTH // 3, HEIGHT // 2)

# Create sprite groups
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            # Change sprite colors when custom event is triggered
            sprite1.change_color(BLUE)
            sprite2.change_color(BLUE)

    # Fill the screen with white color
    screen.fill(WHITE)

    # Update and draw all sprites
    all_sprites.update()
    all_sprites.draw(screen)

    # Refresh the display
    pygame.display.flip()

    # Trigger the custom event after 2 seconds
    pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)

    # Control frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()
sys.exit()
