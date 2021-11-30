class Drop {
  constructor() {
    this.x = random(width);
    this.y = random(-500, -50);
    this.z = random(0, 20);
    // if the drop is closer its faster
    // if its far away, its slower
    this.ySpeed = map(this.z, 0, 20, 2, 12);
    // if the drop is closer its length is bigger
    // if its far away, its length is shorter
    this.length = map(this.z, 0, 20, 5, 10);
  }
  
  show () {
    // if the drop is closer its thicker
    // if its far away, its lighter
    const thickness = map(this.z, 0, 20, 1, 3);
    
    stroke(255, 16, 240, 200);
    strokeWeight(thickness);
    line(this.x, this.y, this.x, this.y + this.length);
  }
  
  fall () {
    // to make the rain fall
    this.y += this.ySpeed;
    
    // to add gravity effect
    const gravity = map(this.z, 0, 20, 0.05, 0.2);
    this.ySpeed += gravity;
    
    // reset the y coordinate to make the
    // rain continous
    if (this.y > height) {
      this.y = random(-200, -100);
      
      this.ySpeed = map(this.z, 0, 20, 2, 12);
    }
  }
}