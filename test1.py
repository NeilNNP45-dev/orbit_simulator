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
planet_x=400
planet_y=150
sun_x = WIDTH//2
sun_y = HEIGHT//2
vx = 9
vy = 0
ax = 0.5
ay = 0.5
G = 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    dx = sun_x - planet_x
    dy = sun_y - planet_y 
    distance = math.sqrt(dx**2 + dy**2 + 100)
    vx += ax * (dx/distance)
    planet_x +=  vx  
    vy += ay * (dy/distance)
    planet_y += vy   
    pygame.draw.circle(screen,(0,0,255),(planet_x, planet_y), 25)
    pygame.draw.circle(screen, (255,255,0), (sun_x, sun_y), 50 )
    if planet_x+50>=WIDTH or planet_x-50<=0:
        vx*= -1
    if planet_y+25>=HEIGHT or planet_y-25<=0:
        y = HEIGHT-25
        vy*= -1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()