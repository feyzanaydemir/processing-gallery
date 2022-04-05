from Star import *

stars = []
speed = 0

def setup():
    size(600, 600)
    
    for i in range(800):
        stars.append(Star())


def draw():
    global speed
    background(0)
    translate(width / 2, height / 2)
    
    speed = map(mouseX, 0, width, 0, 50)
    
    for star in stars:
        star.update(speed)
        star.show() 
