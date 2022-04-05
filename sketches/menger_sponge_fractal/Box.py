class Box():
    def __init__(self, x, y, z, r):
        self.position = PVector(x, y, z)
        self.size = r
    
    
    def show(self):
        push()
        translate(self.position.x, self.position.y, self.position.z)
        fill(150, 0, 255)
        stroke(50, 0, 200, 50)
        strokeWeight(1 + self.size / 40)
        box(self.size)
        pop()
        
        
    def generate(self):
        boxes = []
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    sum = abs(i) + abs(j) + abs(k)
                    
                    # write > 1 to display as classic sponge
                    # write <= 1 to display as opposite
                    if sum > 1:
                        new_size = self.size / 2.5
                        
                        x = self.position.x + i * new_size
                        y = self.position.y + j * new_size
                        z = self.position.z + k * new_size
                        
                        new_box = Box(x, y, z, new_size)
                        boxes.append(new_box)
                        
        return boxes
    
