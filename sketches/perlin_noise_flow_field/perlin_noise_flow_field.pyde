from Particle import *

rows = cols = flow_field = None
particle_count = 300
delta = 0.1
view_scale = 10
z_offset = 0
particles = []


def setup():
    global rows, cols, flow_field
    size(640, 360)
    background(0)
    colorMode(HSB)
    
    for _ in range(particle_count):
        particles.append(Particle())

    rows = floor(width / view_scale) 
    cols = floor(height / view_scale) 
    flow_field = [None] * (rows * cols)

          
def draw():
    global z_offset
    x_offset = 0
    
    for x in range(rows):
        y_offset = 0
        
        for y in range(cols):
            angle = noise(x_offset, y_offset, z_offset) * TWO_PI * 4
            perlin_vector = PVector.fromAngle(angle)
            perlin_vector.setMag(0.5)
            
            # 2D to 1D
            flow_field[y + x * cols] = perlin_vector
            y_offset += delta
        
        x_offset += delta
        z_offset += 0.0005
    
    for particle in particles:
        particle.follow(flow_field, view_scale, cols)
        particle.update()
        particle.wrap()
        particle.show()
