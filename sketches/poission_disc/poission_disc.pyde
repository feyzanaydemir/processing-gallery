k = 30
radius = 4
cell_width = radius / sqrt(2)
grid = []
active_cells = []
ordered_cells = []
rows = cols = None


def setup():
    global rows, cols
    size(400, 400)
    strokeWeight(4)
    colorMode(HSB)
    frameRate(5)
    rows = floor(height / cell_width)
    cols = floor(width / cell_width)
    
    # build a default grid
    for _ in range(rows * cols):
        grid.append(None) # none means no sample
    
    # pick a spot
    x = width / 2
    y = height / 2
    position = PVector(x, y)
    
    i = floor(x / cell_width) # cell's row index at this position
    j = floor(y / cell_width) # cell's col index at this position
    index = i + j * cols # 2D -> 1D array index formula  
    grid[index] = position
    active_cells.append(position)
    
    
def draw():
    background(10)
    
    for total in range(25):
        if len(active_cells) > 0:
            index = floor(random(len(active_cells)))
            position = active_cells[index]
            is_found = False
            
            for n in range(k):
                # create a vector with random direction and radius magnitude
                sample = PVector.random2D()
                mag = random(radius, 2 * radius)
                sample.setMag(mag)
                sample.add(position)
                
                row = floor(sample.y / cell_width)
                col = floor(sample.x / cell_width)
                
                if col > -1 and row > -1 and col < cols and row < rows and not grid[col + row * cols]:
                    is_in_range = True
                    
                    # -1 : cells to the left
                    # 1 : cells to the right
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            neighbor_index = col + i + (row + j) * cols
                            neighbor = grid[neighbor_index]
                            
                            # only if neighbor cell is active
                            if neighbor:
                                distance = PVector.dist(sample, neighbor)
                                
                                if distance < radius:
                                    is_in_range = False
                    
                    if is_in_range:
                        is_found = True
                        
                        grid[col + row * cols] = sample
                        active_cells.append(sample)
                        ordered_cells.append(sample)
                        
                        # maybe?
                        # break
                        
            if not is_found:
                del active_cells[index]
    
    for index, cell in enumerate(ordered_cells):
        if cell:
            stroke(index % 360, 100, 255)
            strokeWeight(5)
            point(cell.x, cell.y)
                        
