from Particle import *

attractor = PVector(250, 250)
particles = []

for _ in range(100):
    particles.append(Particle(PVector(0, 0), PVector.random2D()))


def setup():
    size(500, 500)
    background(255)
    

def draw():
    translate(width/2, height/2)
    stroke(255)
    strokeWeight(10)
    point(attractor.x, attractor.y)
    
    for particle in particles:
        if particle.position.x > 150 and particle.position.y > 150:
            noLoop()
            break
        
        particle.attract(attractor)
        particle.move()
        particle.show()
            
