let sun;

function setup() {
  createCanvas(500, 500);
  
  sun = new Planet(50, 0, 0);
  sun.generateMoons(5, 1);
}

function draw() {
  background(0);
  
  // Center the sun
  translate(width / 2, height / 2);
  sun.show();
  sun.orbit();
}