rows = cols = None
view_width = 2000
view_height = 1600
view_scale = 20
move_coeff = 0
terrain = []

def setup():
    global rows, cols
    size(600, 600, P3D)
    
    rows = view_width / view_scale
    cols = view_height / view_scale
    
    for i in range(rows):
        terrain.append([])
        
        for j in range(cols):
            terrain[i].append(0)
    
    
def draw():
    global move_coeff
    move_coeff -= 0.1
    offset_i = move_coeff
    
    for i in range(rows):
        offset_j = 0
        
        for j in range(cols):
            terrain[i][j] = map(noise(offset_i, offset_j), 0, 1, -60, 60)
            offset_j += 0.3
        
        offset_i += 0.3
    
    background(0)
    translate(600, 300)
    rotateX(PI / 3)
    noFill()
    stroke(255, 80)
    strokeWeight(0.5)
    translate(-view_width / 2, -view_height / 2)
    
    for i in range(rows - 1):
        beginShape(TRIANGLE_STRIP)
        
        for j in range(cols):
            vertex(j * view_scale, i * view_scale, terrain[i][j])
            vertex(j * view_scale, (i + 1) * view_scale, terrain[i + 1][j])
    
        endShape()
