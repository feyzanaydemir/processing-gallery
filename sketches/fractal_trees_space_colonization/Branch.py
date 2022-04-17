class Branch(object):
    def __init__(self, direction, position, parent):
        self.direction = direction
        self.original_direction = self.direction.copy()
        self.position = position
        self.length = 2
        self.parent = parent
        self.count = 0
    
    
    def show(self):
        if self.parent:
            stroke(255)
            strokeWeight(3)
            line(self.position.x, self.position.y, 
                 self.parent.position.x, self.parent.position.y)
    
    
    def get_next(self):
        next_direction = PVector.mult(self.direction, self.length)
        next_position = PVector.add(self.position, next_direction)
        next_branch = Branch(self.direction.copy(), next_position, self)
        
        return next_branch
    
    
    def reset(self):
        self.direction = self.original_direction.copy()
        self.count = 0
        
