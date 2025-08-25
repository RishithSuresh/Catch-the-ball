import pygame
import random

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Catch the Ball")

#colour codes
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# Create simple colored rectangles instead of loading images
def create_basket_surface():
    basket_surface = pygame.Surface((100, 60))
    basket_surface.fill((139, 69, 19))  # Brown color for basket
    pygame.draw.rect(basket_surface, (101, 67, 33), (0, 0, 100, 60), 3)  # Border
    return basket_surface

def create_ball_surface():
    ball_surface = pygame.Surface((40, 40))
    ball_surface.fill(black)  # Transparent background
    ball_surface.set_colorkey(black)  # Make black transparent
    pygame.draw.circle(ball_surface, red, (20, 20), 20)  # Red ball
    pygame.draw.circle(ball_surface, (200, 0, 0), (20, 20), 20, 2)  # Border
    return ball_surface

# Create game objects
basket = create_basket_surface()
ball = create_ball_surface()

# Ball position and properties
ball_x = 380
ball_y = 50
ball_speed = 5
ball_width = 40
ball_height = 40

# Basket position and properties
basket_x = 350
basket_y = 540
basket_speed = 10
basket_width = 100
basket_height = 60

#score
score = 0
font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Move basket with boundary checking
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket_x > 0:
        basket_x -= basket_speed
    if keys[pygame.K_RIGHT] and basket_x < (800 - basket_width):
        basket_x += basket_speed

    # Move ball
    ball_y += ball_speed

    # Check collision with basket
    basket_rect = pygame.Rect(basket_x, basket_y, basket_width, basket_height)
    ball_rect = pygame.Rect(ball_x, ball_y, ball_width, ball_height)

    if basket_rect.colliderect(ball_rect):  # if basket catches ball
        score += 1
        ball_y = 0
        ball_x = random.randint(0, 800 - ball_width)  # Keep ball within screen bounds

    # Reset ball if it goes off screen
    if ball_y > 600:
        ball_y = 0
        ball_x = random.randint(0, 800 - ball_width)  # Keep ball within screen bounds
        
    # Clear screen first
    window.fill(black)

    # Draw game objects
    window.blit(basket, (basket_x, basket_y))
    window.blit(ball, (ball_x, ball_y))

    # Draw score
    text = font.render("Score: " + str(score), True, white)
    window.blit(text, (10, 10))

    # Update display
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
