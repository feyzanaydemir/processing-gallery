def remove_walls(curr, next):
    delta_x = curr.i - next.i
    
    # next cell is on the right of the current one
    if delta_x == 1:
        curr.walls["left"] = False
        next.walls["right"] = False
    # next cell is on the left of the current one
    elif delta_x == -1:
        curr.walls["right"] = False
        next.walls["left"] = False
    
    delta_y = curr.j - next.j
    
    # current cell is under the next one
    if delta_y == 1:
        curr.walls["top"] = False
        next.walls["bottom"] = False
    # next cell is under the current one
    elif delta_y == -1:
        curr.walls["bottom"] = False
        next.walls["top"] = False
        
