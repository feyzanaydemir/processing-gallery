from Branch import *

tree = []
leaves = []
level = 0
angle = PI / 6

def setup():
    global tree
    size(400, 400)
    
    start = PVector(width / 2, height)
    end = PVector(width / 2, height - 100)
    root = Branch(start, end)
    tree.append(root)


def mousePressed():
    global level
    level += 1
    
    for i in range(len(tree) - 1, -1, -1):
        if not tree[i].finished:
            new_branch = tree[i].generate_child_branch(-angle, angle)
            tree += new_branch
            
        tree[i].finished = True
    
    if level > 5:
        for branch in tree:
            if not branch.finished:
                leaf = branch.end.copy()
                leaves.append(leaf)


def move(vector):
    # slightly shake the branch or leaf
    vector.x += random(-0.5, 0.5)
    vector.y += random(-0.5, 0.5)


def draw():
    global tree, leaves
    background(0)
    
    for branch in tree:
        branch.show()
        move(branch.end)
    
    for leaf in leaves:
        fill(255, 0, 100)
        circle(leaf.x, leaf.y, 10)
        move(leaf)
        
