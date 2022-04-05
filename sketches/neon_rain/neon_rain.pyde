from Drop import *

rain = []

def setup():
    size(600, 300)
    
    for i in range(250):
        rain.append(Drop())


def draw():
    background(0, 0, 20)
    
    for drop in rain:
        drop.show()
        drop.fall()
