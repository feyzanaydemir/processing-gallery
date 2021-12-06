class Planet {
  constructor(radius, distance, orbitSpeed = random(0.01, 0.1)) {
    this.radius = radius;
    this.distance = distance;
    this.orbitSpeed = orbitSpeed;
    this.angle = random(0, 3.14);
    this.moons = [];
  }
  
  show() {
    push();
    rotate(this.angle);
    // Arrange distance before drawing
    translate(this.distance, 0);
    fill(255);
    circle(0, 0, this.radius * 2);
    
    if (this.moons.length > 0) {
      for (const moon of this.moons) {
        moon.show();
      }
    }
    
    pop();
  }
  
  generateMoons(count, level) {    
    for (let i = 0; i < count; i++) {
      const newRadius = this.radius / (level * 2);
      const newDistance = random(newRadius + this.radius, (newRadius + this.radius) * 2);
      const newSpeed = random(-0.1, 0.1);
      
      this.moons[i] = new Planet(newRadius, newDistance, newSpeed);
      
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