#!/usr/bin/env python3

import pygame
from PIL import Image, ImageDraw

# -------------------------- Initial variables ---------------------------

# Display size
x_display, y_display = 1000, 500

# Figure movement
x, y = 0, 0 # Where starts
width, height = 40, 60 # sizes
vel = 2 # How fast move

x_cloud, y_cloud = 0, 0 # Coordinates of cloud movements
x_airplane, y_airplane = x_display, 100
# number of the frame
nframe = 0

bombs = []
smoke = []
detonations = []

# Colors
red = (255, 0, 0)
darkgrey = (169, 169, 169)
grey = (128, 128, 128)
dimgrey = (105, 105, 105)
seagreen = (143, 188, 143)
skyblue = (135, 206, 235)
steelblue = (70, 130, 180)
white = (255, 255, 255)
darkorange = (255, 140, 0)
black = (0, 0, 0)


# --------------------------- Functions ---------------------------------
def draw_tree(win, center_pos):
    color = (128, 63, 0)
    x, y = center_pos
    pygame.draw.line(win, color, (x, y), (x, y-50), 5)
    pygame.draw.line(win, color, (x, y-50), (x+20, y-70), 3)
    pygame.draw.line(win, color, (x, y-50), (x-30, y-70), 3)
    pygame.draw.line(win, color, (x, y-50), (x-35, y-55), 3)
    pygame.draw.line(win, color, (x, y-50), (x+35, y-55), 3)
    pygame.draw.line(win, color, (x, y-50), (x+10, y-80), 3)


def draw_cloud(win, center_pos):
    x, y = center_pos
    pygame.draw.ellipse(win, grey, (x, y, 150, 60))
    pygame.draw.ellipse(win, grey, (x + 30, y - 15, 90, 90))

def draw_building(win, pos):
    x, y = pos
    pygame.draw.rect(win, white, (x, y , 80, 150))

    pygame.draw.rect(win, steelblue, (x + 10, y + 15 , 20, 30))
    pygame.draw.rect(win, steelblue, (x + 10, y + 60 , 20, 30))
    pygame.draw.rect(win, steelblue, (x + 10, y + 105 , 20, 30))

    pygame.draw.rect(win, steelblue, (x + 50, y + 15 , 20, 30))
    pygame.draw.rect(win, steelblue, (x + 50, y + 60 , 20, 30))
    pygame.draw.rect(win, steelblue, (x + 50, y + 105 , 20, 30))

def draw_background(win, x_display, y_display):
    pygame.draw.rect(win, dimgrey, [0, 0.9 * y_display, x_display, y_display])
    draw_building(win, (100, 300))
    draw_building(win, (300, 300))
    draw_building(win, (750, 300))

def draw_airplane(win, color, pos):
    x, y = pos

    pygame.draw.rect(win, color, (x + 20, y + 1, 200, 30)) # Drawing a character
    pygame.draw.polygon(win, color, [[x+220, y+1], [x+220, y-20], [x + 200, y-20], [x+190,y+1]])
    pygame.draw.polygon(win, color, [[x+220, y+3], [x + 230, y+7], [x + 230, y + 23], [x+220, y+29]])
    pygame.draw.polygon(win, color, [[x, y + 20], [x + 20, y], [x + 20, y + 30]])

    # - generate PIL image with transparent background -

    pil_size = 22

    pil_image = Image.new("RGBA", (pil_size, pil_size))
    pil_draw = ImageDraw.Draw(pil_image)
    #pil_draw.arc((0, 0, pil_size-1, pil_size-1), 0, 270, fill=red)
    pil_draw.pieslice((0, 0, pil_size-1, pil_size-1), 180, 0, fill=grey)

    # Convert into pygame image
    data = pil_image.tobytes()
    size = pil_image.size
    mode = pil_image.mode

    image = pygame.image.fromstring(data, size, mode)

    image_rect = image.get_rect(center=(x + 100, y + 25))#win.get_rect().center)

    win.blit(image, image_rect)
    
class Bomb:
    def __init__(self, pos_center):
        self.x, self.y = pos_center
        self.draw_bomb()

    def draw_bomb(self):#win, center_pos, rot_var):
        color = (128, 64, 0)
        self.x -= 2
        self.y += 5
        x, y = self.x, self.y
        pygame.draw.polygon(win, color, [[x-12, y-4], [x+12, y-2], [x+12, y+2], [x-12, y+4]])
        pygame.draw.polygon(win, color, [[x+12, y-2], [x+17, y-5], [x+17, y+5], [x+12, y+2]])
        pygame.draw.ellipse(win, color, (x-16, y-3.5, 8, 8))

class Smoke:
    def __init__(self, pos_center):
        self.x, self.y = pos_center
        self.draw_smoke()

    def draw_smoke(self):
        color = (230, 230, 230)
        self.x += 3
        self.y -= 1

        x, y = self.x, self.y
        pygame.draw.polygon(win, color, [[x-12, y-4], [x+12, y-2], [x+12, y+2], [x-12, y+4]])
        pygame.draw.polygon(win, color, [[x+12, y-2], [x+17, y-5], [x+17, y+5], [x+12, y+2]])
        pygame.draw.ellipse(win, color, (x-16, y-3.5, 8, 8))

class Detonation:
    def __init__(self, pos_center):
        self.x, self.y = pos_center
        self.r = 3
        self.draw_explosion()

    def draw_explosion(self):
        color = (255, 90, 0)
        self.r += 2
        x, y, r = self.x, self.y, self.r
        pygame.draw.ellipse(win, color, (x - r, y - r, 2*r, 2*r))

# ----------------------- Initializing pygame ---------------------------

# Initializing pygame
pygame.init()

win = pygame.display.set_mode((x_display, y_display))

pygame.display.set_caption("Simple movement, by Almishev Kostadin")

is_running = True

while is_running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    keys = pygame.key.get_pressed() # Pressed keys
    # key pressing movements
    if keys[pygame.K_LEFT]:
        x -= vel

    if keys[pygame.K_RIGHT]:
        x += vel

    if keys[pygame.K_UP]:
        if y_airplane > 10:
            y_airplane -= vel
        y -= vel

    if keys[pygame.K_DOWN]:
        if y_airplane < y_display / 4:
            y_airplane += vel
        y += vel
    
    # Go to another side
    if x > x_display:
        x = 0
    elif x < -width:
        x = x_display - x - width
    if y > y_display:
        y = 0
    elif y < -height:
        y = y_display - y - height

    # Change movement variables
    x_cloud = (x_cloud + 1) % x_display
    if x_airplane-3<-200:
        x_airplane = x_display-3
    else:
        x_airplane = x_airplane - 3

    nframe += 1

    # Draw all figures
    win.fill(skyblue)

    draw_background(win, x_display, y_display)
    draw_tree(win, (500, y_display*0.9))
    draw_tree(win, (900, y_display*0.9))
    draw_tree(win, (50, y_display*0.9))

    draw_cloud(win, (x_cloud - 100, y_cloud + 20))
    draw_cloud(win, (x_cloud - 400, y_cloud + 90))
    draw_cloud(win, (x_cloud - 800, y_cloud + 80))
    draw_cloud(win, (x_cloud + 100, y_cloud + 80))

    # Drawing smoke after airplane
    smoke.append(Smoke((x_airplane + 140, y_airplane + 12)))
    i = 0
    while i < len(smoke):
        smoke[i].draw_smoke()
        # Remove smoke when goes outside of the screen
        if smoke[i].x > x_display + 20 or smoke[i].y < -5:
            smoke.pop(i)
            i -= 1
        i += 1

    draw_airplane(win, red, (x_airplane - 100, y_airplane))

    # Bomb control -----------------------------------

    # Spawn new bomb
    if (nframe % 40 == 0):
        bombs.append(Bomb((x_airplane + 70, y_airplane + 22)))
    i = 0
    # Draw bombs
    while i < len(bombs):
        bombs[i].draw_bomb()
        # Remove smoke when goes outside of the screen
        if bombs[i].y > y_display*0.9:
            detonations.append(Detonation((bombs[i].x, bombs[i].y)))
            bombs.pop(i)
            i -= 1
        i += 1

    i = 0
    while i < len(detonations):
        detonations[i].draw_explosion()
        if detonations[i].r > 35:
            detonations.pop(i)
            i -= 1
        i += 1

    draw_cloud(win, (x_cloud + 500, y_cloud + 34))
    draw_cloud(win, (x_cloud + 800, y_cloud + 90))

    pygame.display.update()

pygame.quit()