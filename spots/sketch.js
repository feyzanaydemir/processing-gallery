let circleWidth;

function setup() {
  createCanvas(600, 400);
  background(0);
}

function draw() {
  stroke(0, 80);
  strokeWeight(5)
  fill(random(100, 255), 0, random(100, 255), 80);  
  circle(random(width), random(height), random(10, 30));
}