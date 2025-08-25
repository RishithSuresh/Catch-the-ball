import pygame

pygame.init()

window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Catch the Ball")

#colour codes
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

#load images
basket = pygame.image.load("basket.png")
ball = pygame.image.load("ball.png")

#resize images
basket = pygame.transform.scale(basket, (100, 60))
ball = pygame.transform.scale(ball, (40, 40))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(black)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
