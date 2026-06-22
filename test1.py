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
bodies = [sun,planet1,planet2]
ax = 0.5
ay = 0.5
G= 100
def update_physics(bodies):
    sun = bodies[0]
    for body in bodies:
        if body is sun:
            continue
        dx = sun.x - body.x
        dy = sun.y - body.y 
        distance = math.sqrt(dx**2 + dy**2 + 100)
        body.vx += ax * (dx/distance)
        body.x +=  body.vx
        body.vy += ay * (dy/distance)  
        body.y += body.vy
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0,0,0))
    for body in bodies:
        pygame.draw.circle(screen,(body.color),(body.x,body.y),body.radius)
        update_physics(bodies)
    if body.x+body.radius>=WIDTH or body.x-body.radius<=0:
        body.vx*= -1
    if body.y+body.radius>=HEIGHT or body.y-body.radius<=0:
        body.y = HEIGHT-body.radius
        body.vy*= -1
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()