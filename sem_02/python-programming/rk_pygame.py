import pygame
#from math import pi

pygame.init()

BLACK = (0, 0 , 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = [800, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("MY HOME")

done = True
clock = pygame.time.Clock()

def func1(x, y, m, n):
    pygame.draw.ellipse(screen, BLACK, [x, y, m, n], 2)
def func2(x2, y2, r):
    pygame.draw.circle(screen, BLACK, [x2, y2], r, 2)


x, y = 570, 430
m, n = 140, 50
x2, y2 = 640, 400
r = 30



while done:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, [0, 400], [400, 400], 5)
    pygame.draw.line(screen, BLACK, [400, 400], [400, 480], 5)
    pygame.draw.line(screen, BLACK, [400, 480], [800, 480], 5)
    
    pygame.draw.rect(screen, BLACK, [50, 400, 200, -150], 2)
    pygame.draw.rect(screen, BLACK, [80, 350, 50, -50], 2)
    
    pygame.draw.line(screen, BLACK, [80, 325], [130, 325], 2)
    pygame.draw.line(screen, BLACK, [105, 325], [105, 350], 2)

    pygame.draw.circle(screen, BLACK, [200, 325], 30, 2)
    pygame.draw.line(screen, BLACK, [200, 295], [200, 355], 2)
    pygame.draw.line(screen, BLACK, [170, 325], [230, 325], 2)

    
    pygame.draw.rect(screen, RED, [80, 250, 15, -85])
    pygame.draw.polygon(screen, GREEN, [[50, 250], [150, 195], [250, 250]])

    func1(x,y,m,n)
    func2(x2,y2,r)

    x -= 2
    y -= 2
    float m -= 0.05
    float n -= 0.05


    
    x2 -= 2
    y2 -= 2
    float r -= 0.05



    pygame.display.flip()

pygame.quit()
