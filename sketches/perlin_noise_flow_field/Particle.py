class Particle(object):
    def __init__(self):
        self.position = PVector(random(width), random(height))
        self.position_prev = self.position
        self.vel = PVector(0, 0) # velocity
        self.acc = PVector(0, 0) # acceleration
        self.max_speed = 2
    
    
    def show(self):
        stroke(120, 80, 255, 5)
        strokeWeight(3)
        line(self.position.x, self.position.y, self.position_prev.x, self.position_prev.y)
        
        self.update_prev()
    
    
    def update(self):
        self.vel.add(self.acc)
        self.vel.limit(self.max_speed)
        self.position.add(self.vel)
        self.acc.mult(0)
    
    
    def follow(self, vectors, scale, cols):
        x = floor(self.position.x / scale)
        y = floor(self.position.y / scale)
        # formula for converting a 2D value to 1D
        index = x + y * cols
        force = vectors[index]
        
        self.apply_force(force)
    
    
    def wrap(self):
        if self.position.x > width:
            self.position.x = 0
        elif self.position.x < 0:
            self.position.x = width
         
        if self.position.y > height:
            self.position.y = 0
        elif self.position.y < 0:
            self.position.y = height
            
        self.update_prev()
    
    
    def update_prev(self):
        self.position_prev.x = self.position.x
        self.position_prev.y = self.position.y
    
    
    def apply_force(self, force):
        self.acc.add(force)
