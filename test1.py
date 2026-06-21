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
class Body:
    def __init__(self,x,y,vx,vy,color,radius,mass):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radius = radius
        self.mass = mass
planet1 = Body(400,150,9,0,(0,0,255),25,100)
sun = Body(400,300,0,0,(255,255,0),50,10000000)
planet2 = Body(400,50,11,0,(255,0,0),30,5000)
ax = 0.5
ay = 0.5
G= 100
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    dx1 = sun.x - planet1.x
    dy1 = sun.y - planet1.y
    dx2 = sun.x - planet2.x
    dy2 = sun.y - planet2.y 
    distance1 = math.sqrt(dx1**2 + dy1**2 + 100)
    distance2 = math.sqrt(dx2**2 + dy2**2 + 100)
    planet1.vx += ax * (dx1/distance1)
    planet1.x +=  planet1.vx  
    planet1.vy += ay * (dy1/distance1)
    planet1.y += planet1.vy
    planet2.vx += ax * (dx2/distance2)
    planet2.x +=  planet2.vx  
    planet2.vy += ay * (dy2/distance2)
    planet2.y += planet2.vy   
    pygame.draw.circle(screen,planet1.color,(planet1.x, planet1.y), planet1.radius)
    pygame.draw.circle(screen, sun.color, (sun.x, sun.y), sun.radius )
    pygame.draw.circle(screen,planet2.color,(planet2.x, planet2.y), planet2.radius)
    if planet1.x+25>=WIDTH or planet1.x-25<=0:
        planet1.vx*= -1
    if planet1.y+25>=HEIGHT or planet1.y-25<=0:
        planet1.y = HEIGHT-25
        planet1.vy*= -1
    if planet2.x+30>=WIDTH or planet2.x-30<=0:
        planet2.vx*= -1
    if planet2.y+30>=HEIGHT or planet2.y-30<=0:
        planet2.y = HEIGHT-35
        planet2.vy*= -1    
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()