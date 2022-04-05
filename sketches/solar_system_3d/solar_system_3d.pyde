from Planet import *
sun = Planet(70, 0, {"r": 255, "g": 255, "b": 153}, 0)

def setup():
    size(900, 900, P3D)
    sun.generate_moons(5, 1)


def draw():
    background(0)
    lights()
    ambientLight(102, 102, 102)
    pointLight(255, 255, 153, 0, 0, 0)
    translate(width / 2, height / 2)
    sun.show()
    sun.orbit()
