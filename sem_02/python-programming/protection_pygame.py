import pygame
from math import sin, cos, radians

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (800,600)
screen = pygame.display.set_mode(size)

x1 = 100
x2 = 700
y1 = 350
y2 = 300
y3 = 300
y4 = 400
lenth = 50
angle = 0
done = False
clock = pygame.time.Clock()
n = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.fill(WHITE)

    pygame.draw.line(screen, BLACK,[0,400],[800,400],4)
    pygame.draw.circle(screen, BLACK, [x1,y1],50,2)
    pygame.draw.circle(screen, BLACK, [x2,y1],50,2)



    if x2 - x1 == 100:
        n += 1
    if n < 1:

        x1 += 1
        x2 -= 1
        line_x1 = x1 + cos(radians(angle)) * lenth
        line_y1 = y1 + sin(radians(angle)) * lenth
        line_x2 = x1 + cos(radians(angle + 180)) * lenth
        line_y2 = y1 + sin(radians(angle + 180)) * lenth
        line_x3 = x1 + cos(radians(angle + 90)) * lenth
        line_y3 = y1 + sin(radians(angle + 90)) * lenth
        line_x4 = x1 + cos(radians(angle + 270)) * lenth
        line_y4 = y1 + sin(radians(angle + 270)) * lenth


        line2_x1 = x2 + sin(radians(angle + 270)) * lenth
        line2_y1 = y1 + cos(radians(angle + 270)) * lenth
        line2_x2 = x2 + sin(radians(angle+ 90)) * lenth
        line2_y2 = y1 + cos(radians(angle+ 90)) * lenth


    else:
        x1 -= 1
        x2 += 1
        line_x1 = x1 + sin(radians(angle)) * lenth
        line_y1 = y1 + cos(radians(angle)) * lenth
        line_x2 = x1 + sin(radians(angle + 180)) * lenth
        line_y2 = y1 + cos(radians(angle + 180)) * lenth
        line_x3 = x1 + sin(radians(angle + 90)) * lenth
        line_y3 = y1 + cos(radians(angle + 90)) * lenth
        line_x4 = x1 + sin(radians(angle + 270)) * lenth
        line_y4 = y1 + cos(radians(angle + 270)) * lenth
        
        line2_x1 = x2 + cos(radians(angle + 270)) * lenth
        line2_y1 = y1 + sin(radians(angle + 270)) * lenth
        line2_x2 = x2 + cos(radians(angle+ 90)) * lenth
        line2_y2 = y1 + sin(radians(angle+ 90)) * lenth

    pygame.draw.line(screen, BLACK, [x1, y1], [line_x1, line_y1], 2)
    pygame.draw.line(screen, BLACK, [x1, y1], [line_x2, line_y2], 2)
    pygame.draw.line(screen, BLACK, [x2, y1], [line2_x1, line2_y1], 2)
    pygame.draw.line(screen, BLACK, [x2, y1], [line2_x2, line2_y2], 2)
    pygame.draw.line(screen, BLACK, [x1, y1], [line_x3, line_y3], 2)
    pygame.draw.line(screen, BLACK, [x1, y1], [line_x4, line_y4], 2)
    
    angle += 1
        
    pygame.display.flip()
    clock.tick(1)
pygame.quit()
