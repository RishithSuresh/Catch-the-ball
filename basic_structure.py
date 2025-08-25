import pygame

# 1. Initialize pygame (always required before using it)
pygame.init()

# 2. Create a window (width=800, height=600)
window = pygame.display.set_mode((800, 600))

# 3. Set window title
pygame.display.set_caption("Catch the Ball")

# 4. Create a clock object to control frame rate
clock = pygame.time.Clock()

# 5. Game loop (runs continuously until user quits)
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with black (RGB: 0,0,0)
    window.fill((0, 0, 0))

    # Update the display so changes appear
    pygame.display.flip()

    # Control frame rate (60 FPS)
    clock.tick(60)

# 6. Quit pygame properly
pygame.quit()
