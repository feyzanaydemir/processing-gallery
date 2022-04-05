x = 0.01
y = z = 0
coeff_a = 10
coeff_b = 28
coeff_c = 8 / 3
points = []
angle = PI / 3

def setup():
    size(500, 500, P3D)
    colorMode(HSB)


def draw():
    global x, y, z, angle
    # formula : https://wikimedia.org/api/rest_v1/media/math/render/svg/7928004d58943529a7be774575a62ca436a82a7f
    dt = 0.01
    delta_x = (coeff_a * (y - x)) * dt
    delta_y = (x * (coeff_b - z) - y) * dt
    delta_z = (x * y - coeff_c * z) * dt
    
    x += delta_x
    y += delta_y
    z += delta_z
    
    points.append(PVector(x, y, z))
    angle += 0.0025
    
    background(0)
    translate(width / 2, height / 2)
    scale(4)
    stroke(255)
    noFill()
    strokeWeight(3)
    rotateY(angle)
    
    beginShape()
    hu = 0
    
    for vector in points:
        stroke(hu, 255 - hu, 255)
        vertex(vector.x, vector.y, vector.z)
        hu += 0.5
        
        if hu > 255:
            hu = 0
    
    endShape()
    
