from Planet import *

sun = Planet(50, 0, 0)

def setup():
    size(500, 500)
    sun.generate_moons(5, 1)


def draw():
    background(0)
    translate(width / 2, height / 2)
    sun.show()
    sun.orbit()
    
