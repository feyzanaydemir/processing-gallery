function Cell(i, j) {
  this.i = i;
  this.j = j;
  this.visited = false;
  this.walls = {top: true, right: true, bottom: true, left: true}
  
  this.show = function() {
    const coordX = this.i * view;
    const coordY = this.j * view;
    
    stroke(255);
    
    // draw cell walls if they exist
    if (this.walls.top) {
      line(coordX, coordY, coordX + view, coordY);
    }
    
    if (this.walls.right) {
      line(coordX + view, coordY, coordX + view, coordY + view);
    }
    
    if (this.walls.bottom) {
      line(coordX + view, coordY + view, coordX, coordY + view);
    }
    
    if (this.walls.left) {
      line(coordX, coordY + view, coordX, coordY);
    }
    
    if (this.visited) {
      noStroke();
      fill(0);
      rect(coordX, coordY, view, view);
    }
    
  }
  
  this.highlight = function() {
    noStroke();
    fill(255);
    rect(this.i * view, this.j * view, view, view, 20);
  }
  
  this.getNeighbor = function() {
    const neighbors = [];
    
    const top = cells[getNeighborIndex(i - 1, j)];
    const right = cells[getNeighborIndex(i, j + 1)];
    const bottom = cells[getNeighborIndex(i + 1, j)];
    const left = cells[getNeighborIndex(i, j - 1)];
    
    if (top && !top.visited) neighbors.push(top);
    if (right && !right.visited) neighbors.push(right);
    if (bottom && !bottom.visited) neighbors.push(bottom);
    if (left && !left.visited) neighbors.push(left);
    
    if (neighbors.length > 0) {
      const randomNeighbor = floor(random(0, neighbors.length));
    
      return neighbors[randomNeighbor];
    }
  }
}

function getNeighborIndex(i, j) {
  // edge cases (no neighbor)
  if (i < 0 || j < 0 || i > rows - 1 || j > cols - 1) {
    return -1;
  }
    
  return j + i * cols; 
}