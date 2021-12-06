class Star {
  constructor() {
    this.x = random(-width, width);
    this.y = random(-height, height);
    this.z = random(width);
    this.prevZ = this.z;
  }

  show() {
    fill(0, 200, 240, 300);
    noStroke();

    const circleSpreadX = map(this.x / this.z, 0, 1, 0, width);
    const circleSpreadY = map(this.y / this.z, 0, 1, 0, height);
    const diameter = map(this.z, 0, width, 10, 0);
    
    circle(circleSpreadX, circleSpreadY, diameter);

    const lineSpreadX = map(this.x / this.prevZ, 0, 1, 0, width);
    const lineSpreadY = map(this.y / this.prevZ, 0, 1, 0, height);

    this.prevZ = this.z;

    stroke(0, 0, 255, 100);
    line(lineSpreadX, lineSpreadY, circleSpreadX, circleSpreadY);
  }
  
    update() {
    this.z = this.z - speed;
      
    if (this.z < 1) {
      this.x = random(-width, width);
      this.y = random(-height, height);
      this.z = width;
      this.prevZ = this.z;
    }
  }
}