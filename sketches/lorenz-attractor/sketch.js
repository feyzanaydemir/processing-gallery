let x = 0.01;
let y = 0;
let z = 0;
let coeffA = 10;
let coeffB = 28;
let coeffC = 8 / 3;
let points = [];
let angle;

function setup() {
  createCanvas(400, 400, WEBGL);
  colorMode(HSB);
  angle = PI / 3;
}

function draw() {
  let dt = 0.01;
  let deltaX = (coeffA * (y - x)) * dt;
  let deltaY = (x * (coeffB - z) - y) * dt;
  let deltaZ = (x * y - coeffC * z) * dt;
  
  x += deltaX;
  y += deltaY;
  z += deltaZ;
  
  points.push(createVector(x, y, z));
  angle += 0.0025;
  
  background(0);
  translate(0, 0, -80);
  scale(4);
  stroke(255);
  noFill();
  strokeWeight(3);
  rotateY(angle);
  
  beginShape();
  
  let hu = 0;
  
  for (const vector of points) {
    stroke(hu,  255 - hu, 255);
    vertex(vector.x, vector.y, vector.z);
    
    hu += 0.5;
    
    if (hu > 255) {
      hu = 0;
    } 
  }  
  
  endShape();
}