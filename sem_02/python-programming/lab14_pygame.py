import pygame
import sys
from math import sin, cos, radians

BLACK = (0, 0 , 0)
WHITE = (255, 255, 255)

pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("BND")

#def func(x1, y1, m, n, m2, n2, t, s, t2, s2):
#    pygame.draw.circle(screen, BLACK, [x1, y1], 25, 2)
#    pygame.draw.line(screen, BLACK, (m, n), (m2, n2), 2)
#    pygame.draw.line(screen, BLACK, (t, s), (t2, s2), 2)

#def func2(x2, y2):
 #   pygame.draw.circle(screen, BLACK, [x2, y2], 25, 2)
    #pygame.draw.line(screen, BLACK, (0, 450), (700, 450), 4)


x1 = 100
x2 = 700
y1 = 350
y2 = 300


lenth = 50
angle = 0
d = 0

done = True
clock = pygame.time.Clock()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (0, 400), (700, 400), 4)

    pygame.draw.circle(screen, BLACK, [x1, y1], 50, 2)
    pygame.draw.circle(screen, BLACK, [x2, y1], 50, 2)

    if x2 - x1 == 100:
        d += 1
    if d < 1:
        x1 += 1
        x2 -= 1
        line_x1 = x1 + cos(radians(angle)) * lenth
        line_y1 = y1 + sin(radians(angle)) * lenth
        line_x2 = x1 + cos(radians(angle + 180)) * lenth
        line_y2 = y1 + sin(radians(angle + 180)) * lenth

        liner_x1 = x1 + cos(radians(angle)) * lenth
        liner_y1 = y1 + sin(radians(angle)) * lenth
        liner_x2 = x1 + cos(radians(angle - 180)) * lenth
        liner_y2 = y1 + sin(radians(angle - 90)) * lenth

        line2_x1 = x2 + sin(radians(angle + 270)) * lenth
        line2_y1 = y1 + cos(radians(angle + 270)) * lenth
        line2_x2 = x2 + sin(radians(angle + 90)) * lenth
        line2_y2 = y1 + cos(radians(angle + 90)) * lenth
    else:
        x1 -= 1
        x2 += 1
        line_x1 = x1 + sin(radians(angle)) * lenth
        line_y1 = y1 + cos(radians(angle)) * lenth
        line_x2 = x1 + sin(radians(angle + 180)) * lenth
        line_y2 = y1 + cos(radians(angle + 180)) * lenth

        liner_x1 = x1 + cos(radians(angle)) * lenth
        liner_y1 = y1 + sin(radians(angle)) * lenth
        liner_x2 = x1 + cos(radians(angle - 180)) * lenth
        liner_y2 = y1 + sin(radians(angle - 90)) * lenth

        line2_x1 = x2 + cos(radians(angle + 270)) * lenth
        line2_y1 = y1 + sin(radians(angle + 270)) * lenth
        line2_x2 = x2 + cos(radians(angle + 90)) * lenth
        line2_y2 = y1 + sin(radians(angle + 90)) * lenth

    pygame.draw.line(screen, BLACK, [x1, y1], [line_x1, line_y1], 2)
    pygame.draw.line(screen, BLACK, [x1, y1], [line_x2, line_y2], 2)

    pygame.draw.line(screen, BLACK, [x1, y1], [liner_x1, line_y1], 2)
    pygame.draw.line(screen, BLACK, [x1, y1], [liner_x2, line_y2], 2)

    pygame.draw.line(screen, BLACK, [x2, y1], [line2_x1, line2_y1], 2)
    pygame.draw.line(screen, BLACK, [x2, y1], [line2_x2, line2_y2], 2)

    angle += 1

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
