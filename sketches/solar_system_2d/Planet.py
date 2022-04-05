class Planet(object):
    def __init__(self, radius, distance, orbit_speed=random(0.01, 0.05)):
        self.radius = radius
        self.distance = distance
        self.orbit_speed = orbit_speed
        self.angle = random(0, 3.14)
        self.moons = []
    
    
    def show(self):
        push()
        rotate(self.angle)
        # adjust distance before drawing
        translate(self.distance, 0)
        fill(255, 150)
        circle(0, 0, self.radius * 2)
    
        if self.moons:
            for moon in self.moons:
                moon.show()
        
        pop()
    
    
    def generate_moons(self, count, level):
        for i in range(count):
            new_radius = self.radius / (level * 2)
            new_distance = random(new_radius + self.radius, (new_radius + self.radius) * 2)
            new_speed = random(-0.05, 0.05)
            
            self.moons.append(Planet(new_radius, new_distance, new_speed))
            
            if level < 2:
                self.moons[i].generate_moons(int(random(0, 4)), level + 1)
    
    
    def orbit(self):
        self.angle += self.orbit_speed
        
        if self.moons:
            for moon in self.moons:
                moon.orbit()
                
