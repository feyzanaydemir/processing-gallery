let sponge = [];
let angle = 0;
let count = 0;

function setup() {
  createCanvas(400, 400, WEBGL);
  lights();
  // place a  200 x 200 px box in the center of the canvas
  // this is the first box
  sponge.push(new Box(0, 0, 0, 200));
}

function mousePressed() {
  if (count < 3) {
    // update the sponge by adding the generated small boxes
    const nextSponge = [];
  
    // generate small boxes for every small box inside of sponge
    for (const b of sponge) {
      const generatedBoxes = b.generate();
    
      nextSponge.push(...generatedBoxes);
    }
  
    // update the current sponge
    sponge = nextSponge;
    
    count++;
  }
}

function draw() {
  background(0);
  noFill();
  stroke(255);
  
  // slowly rotate the box
  rotateX(angle);
  rotateY(angle * -1);
  angle += 0.01;
  
  for (const elem of sponge) {
    elem.show();
  }
}