class Leaf(object):
    def __init__(self):
        self.position = PVector.random3D().mult(random(width / 2))
        self.reached = False
    
    def show(self):
        fill(255)
        noStroke()
        push()
        translate(self.position.x, self.position.y, self.position.z)
        circle(0, 0, 4)
        pop()
