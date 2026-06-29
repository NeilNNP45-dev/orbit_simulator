class Body:
    def __init__(self,x,y,vx,vy,color,radius,mass,):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.ax = 0
        self.ay = 0
        self.color = color
        self.radius = radius
        self.mass = mass
        self.trail = []
planet1 = Body(500,300,6.1,0,(0,0,255),10,1)
sun = Body(500,500,0,0,(255,255,0),30,7500)
planet2 = Body(500,100,4.3,0,(255,0,0),15,1)
planet3 = Body(500,200,5,0,(180,0,255),12.5,1)
planet4 = Body(500,0,3.8,0,(0,255,255),17,1 )
planet5 = Body(500,400,8.66,0,(255,167,0),9,1)
bodies = [sun,planet1,planet2,planet3,planet4,planet5]