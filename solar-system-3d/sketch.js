let sun;

function setup() {
  createCanvas(500, 500, WEBGL);
  
  sun = new Planet(50, 0, {r: 255, g: 255, b: 153}, 0);
  sun.generateMoons(5, 1);
}

function draw() {
  background(0);
  lights();
  ambientLight(100)
  pointLight(255, 255, 153, 0, 0, 0);
  
  sun.show();
  sun.orbit();
}