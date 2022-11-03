# play with these values
step, loops = 0.01, 20
k, k_limit, direction = 0, 3, 1


def setup():
    size(400, 400)


def draw():
    global k, direction
    beginShape()
    background(50)
    translate(width / 2, height / 2)
    stroke(255)
    strokeWeight(1.5)
    noFill()
    angle, pattern_scale = 0, min(width, height) / 2.5
    
    while angle < TWO_PI * loops:
        r = pattern_scale * cos(k * angle)
        x = r * cos(angle)
        y = r * sin(angle)

        vertex(x, y)
        angle += step
        
    endShape(CLOSE)
    
    if direction == 1:
        if k == k_limit:
            direction = -1
        else:
            k += 0.001
    else:
        if k == 0:
            direction = 1
        else:
            k -= 0.001
    
