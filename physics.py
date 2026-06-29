import math
MAX_TRAIL = 550
G= 1
def compute_accelerations(bodies):  #ill start adding comments now as the project is getting bigger and more complex. This is to calc acceleration. 
    for body in bodies:
        total_ax = 0
        total_ay = 0

        for other_body in bodies:
            if body is other_body:
                continue
            dx = other_body.x - body.x
            dy = other_body.y - body.y
            distance_sq = dx**2 + dy**2 + 1 # 1 is added for softnening so planets dont go crazy when distance between them becomes very small or 0
            distance = math.sqrt(distance_sq)
            a = G * other_body.mass / distance_sq
            total_ax += a * dx / distance
            total_ay += a * dy / distance
        body.ax = total_ax
        body.ay = total_ay
def update_velocities(bodies, factor, sim_dt): # This is to calc velocity.
                                               #Velocity update is split into two half-steps for Leapfrog integration which will improve long-term orbital stability. #
                                               # Factor is used to integrate leapfrog method (update things in 2 phases as velocity and position change acceleration will change too.) for cleaner orbiting than the earlier method (semi euler method)
    for body in bodies:
        body.vx += body.ax * sim_dt * factor
        body.vy += body.ay * sim_dt * factor
def update_positions(bodies,sim_dt): #This is to calc position of bodies. pretty understandable i think on its own.
    for body in bodies:
        body.x += body.vx * sim_dt
        body.y += body.vy * sim_dt
        body.trail.append((body.x, body.y))
        if len(body.trail) > MAX_TRAIL: # This so trails dont keep going on forever and use a lot of ram
            body.trail.pop(0)