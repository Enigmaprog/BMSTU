import pygame
from math import pi

pygame.init()

BLACK = (0, 0 , 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = [400, 300]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("I am legend")

done = True
clock = pygame.time.Clock()

def func1(x, y):
    pygame.draw.lines(screen, BLACK, False, [[x, y], [x+50, y-70], [x+200, y], [x+220, y-50]], 3)

x, y = 0, 80

while done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.fill(WHITE)
    # линия
    pygame.draw.line(screen, GREEN, [0, 0], [50, 50], 5)
    func1(x,y)
    x += 1
    if x == 400:
        x = -220

    # тонкая линия
    pygame.draw.aaline(screen, GREEN, [0, 50], [50, 80], True)
    # пустой прямоугольник
    pygame.draw.rect(screen, BLACK, [75, 10, 50, 20], 2)
    # прямоугольник
    pygame.draw.rect(screen, BLACK, [150, 10, 50, 20])
    # пустой элипс
    pygame.draw.ellipse(screen, RED, [225, 10, 50, 20], 2)
    # элипс
    pygame.draw.ellipse(screen, RED, [300, 10, 50, 20])
    # триугольник
    pygame.draw.polygon(screen, BLACK, [[100, 100], [0, 200], [200, 200]], 5)
    # круг
    pygame.draw.circle(screen, BLUE, [100,250], 40)
    # частности дуг
    pygame.draw.arc(screen, BLACK, [210, 75, 150, 150], 0, pi / 2, 2)
    pygame.draw.arc(screen, GREEN, [210, 75, 150, 150], pi / 2, pi, 2)
    pygame.draw.arc(screen, BLUE, [210, 75, 150, 150], pi, 3 * pi / 2, 2)
    pygame.draw.arc(screen, RED, [210, 75, 150, 150], 3 * pi / 2, 2 * pi, 2)

    pygame.display.flip()

pygame.quit()