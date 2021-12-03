class Planet {
  constructor(radius, distance, color, orbitSpeed = random(0.01, 0.1)) {
    this.radius = radius;
    this.distance = distance;
    this.vector = p5.Vector.random3D().mult(this.distance);
    this.color = color;
    this.orbitSpeed = orbitSpeed;
    this.angle = random(0, 3.14);
    this.moons = [];
  }
  
  show() {
    // temporarily reset drawing state
    push();

    const crossV = this.vector.cross(createVector(1, 0, 1));
    
    // length of the vector must be > 0
    if (crossV.x || crossV.y || crossV.z) {
      rotate(this.angle, crossV);
    }
    
    // arrange distance before drawing
    translate(this.vector.x, this.vector.y, this.vector.z);
    
    fill(this.color.r, this.color.g, this.color.b);
    noStroke();
    sphere(this.radius);
    
    if (this.moons.length > 0) {
      for (const moon of this.moons) {
        moon.show();
      }
    }
    
    pop();
  }
  
  generateMoons(count, level) {    
    for (let i = 0; i < count; i++) {
      const newRadius = this.radius / (level * 3);
      const newDistance = random((newRadius + this.radius) * 2, (newRadius + this.radius) * 3);
      const newSpeed = random(-0.1, 0.1);
      const newColor = {r: random(50, 200), g: random(100, 255), b: random(100, 255)};
      
      this.moons[i] = new Planet(newRadius, newDistance, newColor, newSpeed);
      
      if (level < 2) {
        this.moons[i].generateMoons(random(0, 4), level + 1);
      }
    }
  }
  
  orbit() {
    this.angle += this.orbitSpeed;
    
    if (this.moons.length > 0) {
      for (const moon of this.moons) {
        moon.orbit();
      }
    }
  }
}