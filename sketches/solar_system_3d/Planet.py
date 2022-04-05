class Planet(object):
    def __init__(self, radius, distance, color, speed=random(0.01, 0.1)):
        self.radius = radius
        self.distance = distance
        self.vector = PVector.random3D().mult(self.distance)
        self.color = color
        self.speed = speed
        self.angle = random(TWO_PI)
        self.moons = []
        
        
    def show(self):
        push()
        v1 = PVector(self.vector.x, self.vector.y, self.vector.z)
        v2 = v1.cross(PVector(1, 0, 1))
        rotate(self.angle, v2.x, v2.y, v2.z)

        # Adjust distance before drawing
        translate(self.vector.x, self.vector.y, self.vector.z)
        noStroke()
        fill(self.color["r"], self.color["g"], self.color["b"])
        sphere(self.radius)
        
        if self.moons:
            for moon in self.moons:
                moon.show()
        
        pop()
        
        
    def generate_moons(self, count, level):
        for i in range(count):
            new_radius = self.radius / (level * 1.75)
            new_distance = random((new_radius + self.radius) * 1.25, (new_radius + self.radius) * 3)
            new_color = {"r": int(random(50, 200)), "g": int(random(100, 255)), "b": int(random(100, 255))}
            new_speed = random(-0.1, 0.1)
            
            self.moons.append(Planet(new_radius, new_distance, new_color, new_speed))

            if level < 3:
                self.moons[i].generate_moons(int(random(0, 4)), level + 1)
    
    
    def orbit(self):
        self.angle += self.speed
    
        if self.moons:
            for moon in self.moons:
                moon.orbit()
                
