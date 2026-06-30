import pygame
class Camera:
    def __init__(self, x, y, zoom, width, height):
        self.x = x
        self.y = y
        self.zoom = zoom
        self.width = width
        self.height = height
    def update(self, keys, dt):
     if keys[pygame.K_i]:
        self.zoom*= 1.01
     if keys[pygame.K_o]:
        self.zoom/= 1.01  
     if keys[pygame.K_a]:
        self.x -= 300*dt / self.zoom
     if keys[pygame.K_d]:
        self.x += 300*dt / self.zoom
     if keys[pygame.K_w]:
        self.y -= 300*dt / self.zoom
     if keys[pygame.K_s]:
        self.y += 300*dt / self.zoom    

    def world_to_screen(self, x, y):
        sx = (x - self.x)* self.zoom + self.width/2
        sy = (y - self.y)* self.zoom + self.height/2 
        return sx,sy   
    def screen_to_world(self,sx,sy):
        x =(sx - self.width/2)/self.zoom + self.x
        y =(sy - self.height/2)/self.zoom + self.y
        return x,y