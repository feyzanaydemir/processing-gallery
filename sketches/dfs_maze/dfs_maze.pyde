from Cell import *
from remove_walls import *

rows = cols = current = None
cells = []
stack = []
view = 15

def setup():
    global rows, cols, current
    size(500, 500)
    
    rows = floor(width / view)
    cols = floor(height / view)
    
    for i in range(rows):
        for j in range(cols):
            cells.append(Cell(i, j))

    current = cells[0]    


def draw():
    global current
    background(50)
    
    for cell in cells:
        cell.show(view)
        
    current.visited = True
    current.highlight(view)
    next = current.get_neighbor(cells, rows, cols)
    
    if next is not None:
        next.visited = True
        stack.append(current)
        remove_walls(current, next)
        current = next
    elif stack:
        current = stack.pop()
        
