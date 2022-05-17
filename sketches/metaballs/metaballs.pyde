from Ball import *

balls = []
amount = 9
view_scale = 20

def setup():
    size(600, 400)
    colorMode(HSB)
    
    for _ in range(amount):
        balls.append(Ball(random(width), random(height)))


def draw():
    background(20)
    loadPixels()
    
    for x in range(width):
        for y in range(height):
            sum = 0
            
            for ball in balls:
                delta_x = x - ball.pos.x
                delta_y = y - ball.pos.y
                distance = dist(x, y, ball.pos.x, ball.pos.y)
                
                sum += view_scale * ball.r / distance
            
            pixels[x + y * width] = color(sum, 255, 255)
    
    updatePixels()
    
    for ball in balls:
        #ball.show()
        ball.update()
