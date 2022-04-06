class Branch(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.finished = False
    
    
    def show(self):
        stroke(255)
        line(self.start.x, self.start.y, self.end.x, self.end.y)
    
    
    def generate_child_branch(self, left_angle, right_angle):
        # create a direction vector pointing from start to end
        direction = PVector.sub(self.end, self.start).mult(0.7)

        direction.rotate(left_angle)
        left_end = PVector.add(self.end, direction)
        left = Branch(self.end, left_end)
        
        direction.rotate(-left_angle + right_angle)
        right_end = PVector.add(self.end, direction)
        right = Branch(self.end, right_end)
        
        return [left, right]
        
