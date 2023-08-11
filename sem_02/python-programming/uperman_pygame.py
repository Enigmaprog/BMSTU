import pygame, sys
import time
import math

def draw_tree(x,y):
    #tree trunk (50 wide and 100 tall)
    pygame.draw.rect(screen,(117,90,0),(x,y-100,25,100))
    #leaves are a circle
    pygame.draw.circle(screen,(27,117,0),(x+13,y-120),50)
          
def draw_cloud(x,y,size):
    #put int() around any multiplications by decimals to get rid of this warning:
    #DeprecationWarning: integer argument expected, got float
    pygame.draw.circle(screen,(255,255,255),(x,y),int(size*.5))
    pygame.draw.circle(screen,(255,255,255),(int(x+size*.5),y),int(size*.6))
    pygame.draw.circle(screen,(255,255,255),(x+size,int(y-size*.1)),int(size*.4))

def draw_house(x,y):
    #pink house
    pygame.draw.rect(screen,(255,171,244),(x,y-350,200,350))
    pygame.draw.rect(screen,(0,0,0),(x,y-350,200,350),2)
    #brown door
    pygame.draw.rect(screen,(89,71,0),(x+80,y-60,40,60))
    #yellow door knob
    pygame.draw.circle(screen,(255,204,0),(x+112,y-30),4)
    draw_window(x+20,y-90)
    draw_window(x+130,y-90)
    draw_window(355,235)
    draw_window(245,320)
    draw_window(245,235)
    draw_window(355,320)

def draw_window(x,y):
    #glass
    pygame.draw.rect(screen,(207,229,255),(x,y-50,50,50))
    #frame
    pygame.draw.rect(screen,(0,0,0),(x,y-50,50,50),5)
    pygame.draw.rect(screen,(0,0,0),(x+23,y-50,5,50))
    pygame.draw.rect(screen,(0,0,0),(x,y-27,50,5))

def draw_supermen(x,y):
    #draw red scarf
    pygame.draw.polygon(screen,(255,0,0), [[x,y+2],[x-20,y+60],[x+20,y+60]])
    #draw hands
    pygame.draw.line(screen,(0,0,0),(x,y+10),(x-20,y+35),5)
    pygame.draw.line(screen,(0,0,0),(x,y+10),(x+20,y+35),5)
    #draw body
    pygame.draw.circle(screen,(0,0,0),(x,y), 10)
    pygame.draw.line(screen,(0,0,0),(x,y+13),(x,y+42),10)
    pygame.draw.line(screen,(255,255,255),(x-9,y-4),(x+8,y-4),3)
    #draw legs
    pygame.draw.line(screen,(0,0,0),(x,y+35),(x-15,y+70),5)
    pygame.draw.line(screen,(0,0,0),(x,y+35),(x+15,y+70),5)

def draw_supermen2(x,y):
    #draw red scarf
    pygame.draw.polygon(screen,(255,0,0), [[x,y+2],[x-20,y+60],[x+20,y+60]])
    #draw hands
    pygame.draw.line(screen,(0,0,0),(x,y+15),(x-15,y),5)
    pygame.draw.line(screen,(0,0,0),(x-15,y),(x-15,y-20),4)
    pygame.draw.line(screen,(0,0,0),(x,y+10),(x+20,y+35),5)
    #draw body
    pygame.draw.circle(screen,(0,0,0),(x,y), 10)
    pygame.draw.line(screen,(0,0,0),(x,y+13),(x,y+42),10)
    pygame.draw.line(screen,(255,255,255),(x-9,y-4),(x+8,y-4),3)
    #draw legs
    pygame.draw.line(screen,(0,0,0),(x,y+35),(x-15,y+70),5)
    pygame.draw.line(screen,(0,0,0),(x,y+35),(x+15,y+70),5)

def draw_bubble(x,y):
    pygame.draw.circle(screen,(255,204,0),(x,y-10),10)
    pygame.draw.line(screen,(255,0,0),(x,y),(x,y+20),2)

pygame.init()
screen = pygame.display.set_mode((900,580),0,32)
pygame.display.set_caption("FAKE $UPERMAN")

xCloud1, yCloud1 = 60, 120
xCloud2, yCloud2 = 200, 50
xCloud3, yCloud3 = 550, 100
x_Bubble, y_Bubble = 635, 210
x_Superman, y_Superman = 550, 450
newx_Bubble, newy_Bubble = 535, 410
newx_Superman, newy_Superman = 550, 100

cloudCounter = 0

fall = False
stop = False
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #green ground
    pygame.draw.rect(screen,(0,160,3),(0,500,900,80))
    #light blue sky
    pygame.draw.rect(screen,(135,255,255),(0,0,900,500))
    #yellow sun
    pygame.draw.circle(screen, (255,204,0),(10,10),50)
    #x and y location are the bottom left of tree trunk
    draw_tree(60,500) 
    draw_tree(650,500)
    #draw different clouds

    draw_cloud(xCloud1,yCloud1,80)
    draw_cloud(xCloud2,yCloud2,40)
    draw_cloud(xCloud3,yCloud3,120)
    xCloud1 +=2
    xCloud2 += 2
    xCloud3 += 2
    if xCloud1 == 900: 
        xCloud1 = 0
    elif xCloud2 ==900:
        xCloud2 = 0
    elif xCloud3 == 900:
        xCloud3 = 0
    if cloudCounter >= 0 and cloudCounter < 20:
        yCloud1 += 1
        yCloud2 -= 1
        yCloud3 += 1
        cloudCounter += 1
    elif cloudCounter < 0 and cloudCounter > -20:
        yCloud1 -= 1
        yCloud2 += 1
        yCloud3 -= 1
        cloudCounter -= 1
    elif cloudCounter == 20:
        cloudCounter = -1
    elif cloudCounter == -20:
        cloudCounter = 0
        
    
    draw_house(225,500)

    if stop:
        draw_supermen(550, 450)
    else:
        if fall:
            draw_supermen2(newx_Superman, newy_Superman)
            newy_Superman += 4
            draw_bubble(newx_Bubble,newy_Bubble)
            newy_Bubble -= 2
            #supermen stops in the ground
            if newy_Superman == 452:
                stop = True
        else:
            if x_Bubble == 535 and y_Bubble == 410:
                #supermen raise the hand and goes up
                draw_supermen2(x_Superman, y_Superman)
                y_Superman -= 2
                #bubble goes up
                draw_bubble(newx_Bubble,newy_Bubble)
                newy_Bubble -= 2
                #supermen starts falling 
                if y_Superman == 100:
                    fall = True
            else:
                draw_supermen(x_Superman, y_Superman)
                draw_bubble(x_Bubble,y_Bubble)
                x_Bubble -= 1
                y_Bubble += 2
    
 
        
    time.sleep(0.05)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
sys.exit()
#Developed by Yatagani.K
