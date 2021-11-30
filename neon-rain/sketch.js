let rain = [];

function setup() {
  createCanvas(600, 300);
  
  for (let i = 0; i < 250; i++) {
    rain[i] = new Drop();
  }
}

function draw() {
  background(0, 0, 20);
  
  for (const drop of rain) {
    drop.show();
    drop.fall();
  }
}