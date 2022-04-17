class Leaf(object):
    def __init__(self, position):
        self.position = position
        self.reached = False
    
    
    def show(self):
        fill(255)
        noStroke()
        circle(self.position.x, self.position.y, 4)
        
