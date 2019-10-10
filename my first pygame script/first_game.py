import pygame
import time

pygame.init()

win = pygame.display.set_mode((800,800))
pygame.display.set_caption("first")

x = 50
y = 50
rad = 50
velocity = 5

run = True
while run:
    # controls refreshment rate
    pygame.time.delay(50)

    # check for events
    for event in pygame.event.get():
        # quit if user clicks on red cross
        if event.type == pygame.QUIT:
            run = False

    # check for pressed keys
    keys = pygame.key.get_pressed()

    if(keys[pygame.K_LEFT] and x > 0):
        x -= velocity
    if(keys[pygame.K_RIGHT] and x < 800):
        x += velocity
    if(keys[pygame.K_UP] and y > 0):
        y -= velocity
    if(keys[pygame.K_DOWN] and y < 800):
        y += velocity

    # fill screen with black to hide previous circle
    win.fill((0,0,0))


    # draw a new circle
    pygame.draw.circle(win, (0,255,0), (x, y), rad)

    # update display
    pygame.display.update()

pygame.quit()
