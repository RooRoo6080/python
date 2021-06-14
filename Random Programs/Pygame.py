import pygame, sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
pygame.draw.circle(screen, [0, 0, 250], [320, 240], 100, 0)
pygame.draw.rect(screen, [0, 0, 100], (200, 150, 100, 50), 10)
pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
