class Star(object):
    def __init__(self):
        self.x = random(-width, width)
        self.y = random(-height, height)
        self.z = random(width)
        self.prev_z = self.z
    
    
    def show(self):
        fill(0, 200, 240, 300)
        noStroke()
    
        circle_spread_x = map(self.x / self.z, 0, 1, 0, width)
        circle_spread_y = map(self.y / self.z, 0, 1, 0, height)
        diameter = map(self.z, 0, width, 10, 0)
        
        circle(circle_spread_x, circle_spread_y, diameter)
    
        line_spread_x = map(self.x / self.prev_z, 0, 1, 0, width)
        line_spread_y = map(self.y / self.prev_z, 0, 1, 0, height)
    
        self.prev_z = self.z
    
        stroke(0, 0, 255, 100)
        line(line_spread_x, line_spread_y, circle_spread_x, circle_spread_y)
    
    
    def update(self, speed):
        self.z = self.z - speed
        
        if self.z < 1:
            self.x = random(-width, width)
            self.y = random(-height, height)
            self.z = width
            self.prev_z = self.z
            
