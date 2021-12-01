let stars = [];
let speed;

function setup() {
  createCanvas(500, 500);
  for (let i = 0; i < 600; i++) {
    stars[i] = new Star();
  }
}

function draw() {
   background(0);
  
  speed = map(mouseX, 0, width, 0, 50);
  
  translate(width / 2, height / 2);
  
  for (let i = 0; i < stars.length; i++) {
    stars[i].update();
    stars[i].show();
  }
}