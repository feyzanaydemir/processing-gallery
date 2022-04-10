from Tree import *

tree = None
angle = PI / 6

def setup():
    global tree
    size(600, 600, P3D)
    tree = Tree(300, 50)


def draw():
    global angle
    angle += 0.01
    background(30)
    translate(width / 2, height / 2)
    rotateY(angle)
    
    tree.show()
    tree.grow(50, 1)
    
