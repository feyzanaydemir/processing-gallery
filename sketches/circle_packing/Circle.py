class Circle(object):
    def __init__(self, x, y, colour):
        self.pos = PVector(x, y)
        self.r = 0
        self.colour = colour
        self.is_growing = True
   
    
    def show(self):
        fill(self.colour)
        circle(self.pos.x, self.pos.y, self.r * 2)
        
    
    def grow(self):
        if self.is_growing and self.r < 10:
            self.r += 1
            
            
    def is_touching_edges(self):
        return (self.pos.x + self.r > width or self.pos.x - self.r < 0
                or self.pos.y + self.r > height or self.pos.y - self.r < 0)
        
        
