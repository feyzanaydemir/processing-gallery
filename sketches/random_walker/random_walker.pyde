position = PVector(200, 200, 0)
prev_position = position.copy()


def setup():
    size(400, 400, P3D)
    background(50)


def draw():
    global position
    stroke(255, 100)
    strokeWeight(2)
    line(prev_position.x, prev_position.y, prev_position.z, position.x, position.y, position.z)

    # get random direction
    step = PVector.random3D()

    if random(100) < 2: step.mult(random(20, 50))
    else: step.setMag(3)
    
    prev_position.set(position)
    position.add(step)
