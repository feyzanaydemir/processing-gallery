class Drop(object):
    def __init__(self):
        self.x = random(width)
        self.y = random(-500, -50)
        self.z = random(0, 20)
        
        # the drop is faster if it's closer 
        # it's slower if it's far away 
        self.y_speed = map(self.z, 0, 20, 2, 12)
        
        # the drops length is bigger if it's closer
        # it's length is shorter if it's far away
        self.length = map(self.z, 0, 20, 5, 10)
    
    
    def show(self):
        stroke(255, 16, 240, 200)
        # if the drop is closer it's thicker
        # if it's far away, it's lighter
        thickness = map(self.z, 0, 20, 1, 3)
        strokeWeight(thickness)
        line(self.x, self.y, self.x, self.y + self.length)
        
    
    def fall(self):
        # to make the rain fall
        self.y += self.y_speed
        # to add gravity effect
        gravity = map(self.z, 0, 20, 0.05, 0.2)
        self.y_speed += gravity
        
        # reset the y coordinate to make the rain continous
        if self.y > height:
            self.y = random(-200, -100)
        
        self.y_speed = map(self.z, 0, 20, 2, 12)
        
