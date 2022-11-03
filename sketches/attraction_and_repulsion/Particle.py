class Particle(object):
    def __init__(self, position, velocity):
        self.position = position
        self.prev_position = position.copy()
        self.velocity = velocity
        self.acceleration = PVector()
    
    
    def show(self):
        stroke(0, 30)
        strokeWeight(2)
        line(self.position.x, self.position.y, self.prev_position.x, self.prev_position.y)
        
        self.prev_position.x = self.position.x 
        self.prev_position.y = self.position.y
        
    
    def move(self):
        self.position.add(self.velocity)
        self.velocity.add(self.acceleration)
    
    
    def attract(self, target):
        direction = target.sub(self.position)
        magnitude = 0.1
        direction.setMag(magnitude)
        self.acceleration = direction
        
