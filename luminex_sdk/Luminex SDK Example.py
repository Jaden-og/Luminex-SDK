import luminex_sdk
import pygame

# Initialize Pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Luminex SDK Example")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
