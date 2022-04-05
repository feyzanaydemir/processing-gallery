class Cell(object):
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.visited = False
        self.walls = {"top": True, "right": True, "bottom": True, "left": True}
        
        
    def show(self, view):
        x = self.i * view
        y = self.j * view
        
        stroke(255)
        
        # draw cell walls if they exist
        if self.walls["top"]:
            line(x, y, x + view, y)
        if self.walls["right"]:
            line(x + view, y, x + view, y + view)
        if self.walls["bottom"]:
            line(x + view, y + view, x, y + view)
        if self.walls["left"]:
            line(x, y + view, x, y)
            
        if self.visited:
            noStroke()
            fill(0)
            rect(x, y, view, view)
    
    
    def highlight(self, view):
        noStroke()
        fill(255)
        rect(self.i * view, self.j * view, view, view, 20)
        
        
    @staticmethod
    def get_neighbor_index(i, j, rows, cols):
        # edge cases (no neighbor)
        if i < 0 or j < 0 or i > rows - 1 or j > cols - 1:
            return -1
        return j + i * cols
    
    
    def get_neighbor(self, cells, rows, cols):
        neighbors = []
        
        top = cells[self.get_neighbor_index(self.i - 1, self.j, rows, cols)]
        right = cells[self.get_neighbor_index(self.i, self.j + 1, rows, cols)]
        bottom = cells[self.get_neighbor_index(self.i + 1, self.j, rows, cols)]
        left = cells[self.get_neighbor_index(self.i, self.j - 1, rows, cols)]
        
        if top and not top.visited:
            neighbors.append(top)
        if right and not right.visited:
            neighbors.append(right)
        if bottom and not bottom.visited:
            neighbors.append(bottom)
        if left and not left.visited:
            neighbors.append(left)
        
        if neighbors:
            random_index = floor(random(0, len(neighbors)))
            
            return neighbors[random_index]
        
