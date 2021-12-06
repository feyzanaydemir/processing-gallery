let rows, cols;
let terrain = [];
let viewScale = 10;
let viewWidth = 1200;
let viewHeight = 1200;
let moveCoeff = 0;

function setup() {
  createCanvas(500, 500, WEBGL);
  
  rows = viewWidth / viewScale;
  cols = viewHeight / viewScale;
  
  for (let i = 0; i < rows; i++) {
    terrain[i] = [];
    
    for (let j = 0; j < cols; j++) {
      terrain[i][j] = 0;
    }
  }
}

function draw() {
  moveCoeff -= 0.1;
  
  let offsetI = moveCoeff;

  for (let i = 0; i < rows; i++) {
    let offsetJ = 0;
    
    for (let j = 0; j < cols; j++) {
      terrain[i][j] = map(noise(offsetI, offsetJ), 0, 1, -50, 50);
      
      offsetJ += 0.2;
    }
    
    offsetI += 0.2;
  }
  
  background(0);
  translate(0, 50);
  rotateX(PI / 3);
  noFill();
  stroke(255, 80);
  strokeWeight(0.5);
  translate(-viewWidth / 2 , -viewHeight / 2);
  
  for (let i = 0; i < rows - 1; i++) {
    beginShape(TRIANGLE_STRIP);
    
    for (let j = 0; j < cols; j++) {
      vertex(j * viewScale, i * viewScale, terrain[i][j]);
      vertex(j * viewScale, (i + 1) * viewScale, terrain[i + 1][j]);
    }
    
    endShape();
  }
}