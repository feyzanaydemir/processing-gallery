class Ball(object):
    def __init__(self, x, y):
        angle = random(0, TWO_PI)
        
        self.pos = PVector(x, y)
        self.x_speed = random(50, 90) * cos(angle)
        self.y_speed = random(50, 90) * sin(angle)
        self.r = random(100, 200)

    
    def show(self):
        noFill()
        stroke(0)
        strokeWeight(4)
        #stroke(255)
        ellipse(self.pos.x, self.pos.y, self.r * 2, self.r * 2)
        
    
    def update(self):
        self.pos.x += self.x_speed
        self.pos.y += self.y_speed
        
        if self.pos.x > width or self.pos.x < 0:
            self.x_speed *= -1
            
        if self.pos.y > height or self.pos.y < 0:
            self.y_speed *= -1
            
