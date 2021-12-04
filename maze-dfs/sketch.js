let row, cols, current;
let view = 20;
let cells = [];
let stack = [];

function setup() {
  createCanvas(600, 600);

  rows = floor(width / view);
  cols = floor(height / view);
  
  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      cells.push(new Cell(i, j));
    }
  }
  
  // initilize current cell
  current = cells[0];
}

function draw() {
  background(50);
  
  for (const cell of cells) {
    cell.show();
  }
  
  current.highlight();
  current.visited = true;
  
  const next = current.getNeighbor();

  if (next) {
    stack.push(current);
    
    removeWalls(current, next);
    
    current = next;
    
    // backtrack if there are no valid neighbors
  } else if (stack.length > 0) {
    current = stack.pop();
  }
}

function removeWalls(curr, next) {
  const deltaX = curr.i - next.i;
  
  // next cell is on the right of the current one
  if (deltaX === 1) {
    curr.walls.left = false;
    next.walls.right = false;
    
    // next cell is on the left of the current one
  } else if (deltaX === -1) {
    curr.walls.right = false;
    next.walls.left = false;
  }
  
  const deltaY = curr.j - next.j;
  
  // current cell is under the next one
  if (deltaY === 1) {
    curr.walls.top = false;
    next.walls.bottom = false;
    
    // next cell is under the current one
  } else if (deltaY === -1) {
    curr.walls.bottom = false;
    next.walls.top = false;
  }
}