import pygame
import random

# --- Initialize ---
pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Catch the Ball")

# Colours
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
brown = (139, 69, 19)

# --- Create Basket & Ball Surfaces ---
def create_basket_surface():
    basket_surface = pygame.Surface((100, 60))
    basket_surface.fill(brown)  
    pygame.draw.rect(basket_surface, (101, 67, 33), (0, 0, 100, 60), 3)  # Border
    return basket_surface

def create_ball_surface():
    ball_surface = pygame.Surface((40, 40))
    ball_surface.fill(black)
    ball_surface.set_colorkey(black)
    pygame.draw.circle(ball_surface, red, (20, 20), 20)
    pygame.draw.circle(ball_surface, (200, 0, 0), (20, 20), 20, 2)
    return ball_surface

# Game Objects
basket = create_basket_surface()
ball = create_ball_surface()

# Basket properties
basket_x, basket_y = 350, 540
basket_speed = 10
basket_width, basket_height = 100, 60

# Ball properties
ball_x, ball_y = 380, 50
ball_speed = 5
ball_width, ball_height = 40, 40

# Score
score = 0
font = pygame.font.Font(None, 48)

# Clock
clock = pygame.time.Clock()

# --- Game State ---
state = "menu"  # can be "menu", "playing", "game_over"

def reset_game():
    """Reset variables for a new game"""
    global basket_x, basket_y, score, ball_x, ball_y
    basket_x, basket_y = 350, 540
    ball_x, ball_y = random.randint(0, 800 - ball_width), 50
    score = 0

running = True
while running:
    window.fill(black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle key presses for each state
        if state == "menu":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Enter to start
                    reset_game()
                    state = "playing"
                elif event.key == pygame.K_ESCAPE:  # Escape to quit
                    running = False
        
        elif state == "game_over":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart
                    reset_game()
                    state = "playing"
                elif event.key == pygame.K_ESCAPE:  # Quit
                    running = False

    # --- Menu State ---
    if state == "menu":
        title = font.render("Catch the Ball", True, white)
        start_text = font.render("Press ENTER to Start", True, white)
        quit_text = font.render("Press ESC to Quit", True, white)

        # Center the text horizontally
        title_x = (800 - title.get_width()) // 2
        start_x = (800 - start_text.get_width()) // 2
        quit_x = (800 - quit_text.get_width()) // 2

        window.blit(title, (title_x, 150))
        window.blit(start_text, (start_x, 250))
        window.blit(quit_text, (quit_x, 330))
    
    # --- Playing State ---
    elif state == "playing":
        # Basket movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and basket_x > 0:
            basket_x -= basket_speed
        if keys[pygame.K_RIGHT] and basket_x < (800 - basket_width):
            basket_x += basket_speed
        
        # Ball movement
        ball_y += ball_speed
        
        # Collision
        basket_rect = pygame.Rect(basket_x, basket_y, basket_width, basket_height)
        ball_rect = pygame.Rect(ball_x, ball_y, ball_width, ball_height)
        
        if basket_rect.colliderect(ball_rect):
            score += 1
            ball_y = 0
            ball_x = random.randint(0, 800 - ball_width)
        
        # Missed ball → Game Over
        if ball_y > 600:
            state = "game_over"
        
        # Draw objects
        window.blit(basket, (basket_x, basket_y))
        window.blit(ball, (ball_x, ball_y))

        # Draw centered score
        score_text = font.render("Score: " + str(score), True, white)
        score_x = (800 - score_text.get_width()) // 2
        window.blit(score_text, (score_x, 10))
    
    # --- Game Over State ---
    elif state == "game_over":
        over_text = font.render("GAME OVER!", True, red)
        score_text = font.render("Final Score: " + str(score), True, white)
        restart_text = font.render("Press R to Restart", True, white)
        quit_text = font.render("Press ESC to Quit", True, white)

        # Center all game over text horizontally
        over_x = (800 - over_text.get_width()) // 2
        score_x = (800 - score_text.get_width()) // 2
        restart_x = (800 - restart_text.get_width()) // 2
        quit_x = (800 - quit_text.get_width()) // 2

        window.blit(over_text, (over_x, 150))
        window.blit(score_text, (score_x, 210))
        window.blit(restart_text, (restart_x, 290))
        window.blit(quit_text, (quit_x, 350))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
