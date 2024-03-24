# Import a library of functions called 'pygame'
import pygame
from math import pi


pygame.init()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE  = (0, 0, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)


size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Example code for the draw module")

done = False
clock = pygame.time.Clock()

while not done:
    clock.tick(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done=True

    screen.fill(WHITE)

    pygame.draw.arc(screen, BLACK, [210, 75, 150, 125], 0, pi / 2, 2)
    pygame.draw.arc(screen, GREEN, [210, 75, 150, 125], pi / 2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 125], pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen, RED, [210, 75, 150, 125], 3 * pi / 2, 2 * pi, 2)
    pygame.display.flip()

    pygame.quit()
