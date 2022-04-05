from Box import *

sponge = []
angle = 0
count = 0

def setup():
    size(500, 500, P3D)
    lights()
    
    sponge.append(Box(0, 0, 0, 200))


def mousePressed():
    global count
    
    # update the sponge by adding generated small boxes
    if count < 3:
        next_sponge = []
        
        # generate small boxes for every small box inside of sponge
        for box in sponge:
            generated_boxes = box.generate()
            next_sponge += generated_boxes
        
        sponge = next_sponge
        count += 1
    
    
def draw():
    global angle
    background(20)
    noFill()
    stroke(255)
    translate(width / 2, height / 2)
    rotateX(angle)
    rotateY(angle * -1)
    angle += 0.01
    
    for box in sponge:
        box.show()
        
