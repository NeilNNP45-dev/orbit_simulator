import pygame
import sys
import math


pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Playground")

running = True
planet1_x=400
planet1_y=150
planet2_x=400
planet2_y= 50
sun_x = WIDTH//2
sun_y = HEIGHT//2
vx1 = 9
vy1 = 0
vx2 = 11
vy2 = 0
ax1 = 0.5
ay1 = 0.5
ax2 = 0.5
ay2 = 0.5
G = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    dx1 = sun_x - planet1_x
    dy1 = sun_y - planet1_y
    dx2 = sun_x - planet2_x
    dy2 = sun_y - planet2_y 
    distance1 = math.sqrt(dx1**2 + dy1**2 + 100)
    distance2 = math.sqrt(dx2**2 + dy2**2 + 100)
    vx1 += ax1 * (dx1/distance1)
    planet1_x +=  vx1  
    vy1 += ay1 * (dy1/distance1)
    planet1_y += vy1
    vx2 += ax2 * (dx2/distance2)
    planet2_x +=  vx2  
    vy2 += ay2 * (dy2/distance2)
    planet2_y += vy2   
    pygame.draw.circle(screen,(0,0,255),(planet1_x, planet1_y), 25)
    pygame.draw.circle(screen, (255,255,0), (sun_x, sun_y), 50 )
    pygame.draw.circle(screen,(100,10,0),(planet2_x, planet2_y), 30)
    if planet1_x+25>=WIDTH or planet1_x-25<=0:
        vx1*= -1
    if planet1_y+25>=HEIGHT or planet1_y-25<=0:
        planet1_y = HEIGHT-25
        vy1*= -1
    if planet2_x+30>=WIDTH or planet2_x-30<=0:
        vx2*= -1
    if planet2_y+30>=HEIGHT or planet2_y-30<=0:
        planet2_y = HEIGHT-35
        vy2*= -1    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()