import pygame
import sys
from body import Body,bodies
from physics import *
from camera import Camera


pygame.init()

WIDTH = 1280
HEIGHT = 720
camera = Camera(WIDTH/2,HEIGHT/2,1.0,WIDTH,HEIGHT)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()
pygame.display.set_caption("Pygame Playground")

running = True
time_scale = 80

while running:
    dt = (clock.tick(60)/1000)
    sim_dt = dt * time_scale
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
            running = False    
    keys = pygame.key.get_pressed()    
    camera.update(keys, dt)            
    screen.fill((0,0,0))
    compute_accelerations(bodies)          # a(t) 
    update_velocities(bodies, 0.5,sim_dt)  # half step updation of velocity
    update_positions(bodies,sim_dt)        # full position step
    compute_accelerations(bodies)          # a(t+1)
    update_velocities(bodies, 0.5,sim_dt)  # second half step updation of velocity
    for body in bodies:
        for i in range(len(body.trail)-1):
                x1, y1 = body.trail[i]
                x2, y2 = body.trail[i+1]
                sx1, sy1 = camera.world_to_screen(x1, y1)
                sx2, sy2 = camera.world_to_screen(x2, y2)
                pygame.draw.line(screen,body.color,(sx1,sy1),(sx2,sy2),1) 
        scaled_radius = max(1, int(body.radius*camera.zoom))
        sx,sy = camera.world_to_screen(body.x,body.y)               
        pygame.draw.circle(screen,(body.color),(int(sx),int(sy)),scaled_radius)
    hud_lines = [
    f"FPS: {clock.get_fps():.1f}",
    f"Bodies: {len(bodies)}",
    f"Zoom: {camera.zoom:.2f}x",
    f"Time Scale: {time_scale}x",
    f"Integrator: Leapfrog"]
    for i, line in enumerate(hud_lines):
     text_surface = font.render(line, True, (255, 255, 255))
     screen.blit(text_surface, (10, 10 + i * 30))
    pygame.display.flip()
pygame.quit()
sys.exit()