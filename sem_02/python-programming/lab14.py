import pygame
import sys

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BROWN = (138,54,15)
BROWN2 = (205,183,158)
GREEN = (0,205,0)
GREEN2 = (127,255,0)
BLUE = (0,238,238)
BLUE2 = (255,64,64)
YELLOW = (255, 255, 0)
YELLOW2 = (255,215,0)


pygame.init()

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mongolia")

def draw_sun(x,y):
    #pygame.draw.line(screen, YELLOW, startpoint, current_endpoint, 3)
    pygame.draw.line(screen, YELLOW, (x, y), (x, y-65), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x + 40, y - 55), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x + 60, y - 30), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x + 65, y), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x + 60, y + 30), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x + 40, y + 55), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x, y + 65), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x - 40, y + 55), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x - 65, y + 30), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x - 65, y), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x - 40, y - 55), 4)
    pygame.draw.line(screen, YELLOW, (x, y), (x - 60, y - 30), 4)
    pygame.draw.circle(screen, YELLOW2, (x, y), 40)

def draw_mountain(x,y):
    pygame.draw.polygon(screen, GREEN2, [[x - 95, y], [x - 25, y - 100], [x+45, y]])
    pygame.draw.polygon(screen, GREEN2, [[x + 55, y], [x + 125, y - 100], [x + 195, y]])
    pygame.draw.polygon(screen, GREEN2, [[x + 200, y], [x + 270, y - 100], [x + 340, y]])
    pygame.draw.polygon(screen, GREEN2, [[x + 345, y], [x + 415, y - 100], [x + 485, y]])
    pygame.draw.polygon(screen, GREEN2, [[x + 490, y], [x + 560, y - 100], [x + 630, y]])
    pygame.draw.polygon(screen, GREEN2, [[x + 635, y], [x + 705, y - 100], [x + 775, y]])
    pygame.draw.polygon(screen, GREEN, [[x, y], [x + 50, y - 150], [x + 100, y]])
    pygame.draw.polygon(screen, GREEN, [[x + 150, y], [x + 200, y - 150], [x + 250, y]])
    pygame.draw.polygon(screen, GREEN, [[x + 300, y], [x + 350, y - 150], [x + 400, y]])
    pygame.draw.polygon(screen, GREEN, [[x + 450, y], [x + 500, y - 150], [x + 550, y]])
    pygame.draw.polygon(screen, GREEN, [[x + 575, y], [x + 625, y - 150], [x + 675, y]])

def draw_baloon(x,y):
    pygame.draw.rect(screen, BROWN2, (x, y, 60, 40))
    pygame.draw.polygon(screen, BROWN2, [[x, y], [x + 30, y - 40], [x + 60, y]], 4)
    pygame.draw.circle(screen, BLUE2, (x + 30, y - 70), 55)

def draw_cloud(x,y,size):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), int(size * .5))
    pygame.draw.circle(screen, (255, 255, 255), (int(x + size * .5), y), int(size * .6))
    pygame.draw.circle(screen, (255, 255, 255), (x + size, int(y - size * .1)), int(size * .4))

x_baloon, y_baloon = 500, 450
x_mountain, y_mountain = 0, 430
x_sun, y_sun = 100, 100
xCloud1, yCloud1 = 60, 120
xCloud2, yCloud2 = 200, 50
xCloud3, yCloud3 = 550, 100

#startpoint = pygame.math.Vector2(100, 100)
#endpoint = pygame.math.Vector2(150, 30)
#angel = 0

done = True
clock = pygame.time.Clock()

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    screen.fill(BLUE)

    pygame.draw.rect(screen,BROWN,(0,430,700,70))
    draw_mountain(x_mountain, y_mountain)

    draw_sun(x_sun, y_sun)
    x_sun += 1
    if x_sun == 700:
        x_sun = -65

    #angel = (angel+5) % 360
    #current_endpoint = startpoint + endpoint.rotate(angel)

    #pygame.draw.line(screen, YELLOW, startpoint, current_endpoint, 3)
    draw_cloud(xCloud1, yCloud1, 80)
    draw_cloud(xCloud2, yCloud2, 40)
    draw_cloud(xCloud3, yCloud3, 120)
    xCloud1 += 2
    xCloud2 += 2
    xCloud3 += 2
    if xCloud1 == 700:
        xCloud1 = -10
    elif xCloud2 ==700:
        xCloud2 = -10
    elif xCloud3 == 700:
        xCloud3 = -10

    draw_baloon(x_baloon, y_baloon)
    y_baloon -= 3

    pygame.display.flip()
    clock.tick(10)

pygame.quit()
sys.exit(0)