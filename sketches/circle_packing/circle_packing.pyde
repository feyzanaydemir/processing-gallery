from Circle import *

img, circles = None, []


def setup():
    global img
    size(627, 333)
    img = loadImage("starry_night.jpg")
    img.resize(627, 333)
    

def create_circle():
    x, y = random(width), random(height)
    
    for c in circles:
        distance = dist(x, y, c.pos.x, c.pos.y)
        
        if distance < c.r:
            return None
    
    index = int(x) + int(y) * width
    colour = img.pixels[index]
    
    return Circle(x, y, colour)


def add_circles(total):
    count = 0
    attempts, attempts_limit = 0, 1000
    
    while count < total:
        new_circle = create_circle()
        
        if new_circle:
            circles.append(new_circle)
            count += 1
            attempts = 0
        else:
            attempts += 1
            if attempts > attempts_limit:
                noLoop()
                break


def is_overlapping(current):
    for other in circles:
        if current != other:
            distance = dist(current.pos.x, current.pos.y, other.pos.x, other.pos.y)
                        
            if distance - 1.5 < current.r + other.r:
                return True
            
    return False


def draw():
    background(0)
    add_circles(10)
    
    for curr in circles:
        curr.show()
        curr.grow()
        
        if curr.is_growing:
            if curr.is_touching_edges() or is_overlapping(curr):
                curr.is_growing = False
                
