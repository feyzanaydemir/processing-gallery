from Tree import *

max_distance = 50
min_distance = 1
tree = None

def setup():
    global tree
    size(400, 400)
    tree = Tree(500, width, height, max_distance)


def draw():
    background(30)
    tree.show()
    tree.grow(max_distance, min_distance)
    
