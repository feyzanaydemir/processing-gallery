class Box {
  constructor(x, y, z, r) {
    this.position = createVector(x, y, z);
    this.size = r;
  }
  
  show () {
    // initilize a new drawing state
    push();
    
    // set coordinates
    translate(this.position.x, this.position.y, this.position.z);
    
    // draw the box at that position
    fill(150, 0, 255);
    stroke(50, 0, 200, 50);
    strokeWeight(1 + this.size / 40);
    box(this.size);
    
    // Restore original state
    pop();
  }
  
  generate () {
    const boxes = [];
    
    for (let i = -1; i < 2; i++) {
      for (let j = -1; j < 2; j++) {
        for (let k = -1; k < 2; k++) {
          const sum = abs(i) + abs(j) + abs(k);
          
          // write > 1 to display as box
          // write <= 1 to display as snowflake
          if (sum <= 1) {
            // new box's dimensions should be the third of the current one
            const newSize = this.size / 3;
          
            // offset the new coordinates
            const x = this.position.x + i * newSize;
            const y = this.position.y + j * newSize;
            const z = this.position.z + k * newSize;
          
            const newBox = new Box(x, y, z, newSize);
          
            boxes.push(newBox);
          }
        }
      }
    }
    
    return boxes;
  }
}