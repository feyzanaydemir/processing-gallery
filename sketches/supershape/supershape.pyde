# http://paulbourke.net/geometry/supershape/

r = 150
total = 50
globe = [None] * ((total + 1) ** 2)
m = offset = 0
a = b = 1
angle = PI / 4

def supershape(theta, m, n1, n2, n3):
    t1 = abs((1 / a) * cos(m * theta / 4))
    t1 = pow(t1, n2)
    
    t2 = abs((1 / b) * sin(m * theta / 4))
    t2 = pow(t2, n3)
    
    t3 = t1 + t2
    r = pow(t3, -1 / n1)
    
    return r


def setup():
    size(500, 500, P3D)
    colorMode(HSB)


def draw():
    global offset, angle
    background(10)
    # orbitControl()
    noStroke()
    
    for i in range(total + 1):
        lat = map(i, 0, total, -HALF_PI, HALF_PI)
        r2 = supershape(lat, 7, 0.2, 1.7, 1.7)
        
        for j in range(total + 1):
            lon = map(j, 0, total, -PI, PI)
            r1 = supershape(lon, 7, 0.2, 1.7, 1.7)
            
            x = r * r1 * cos(lon) * r2 * cos(lat)
            y = r * r1 * sin(lon) * r2 * cos(lat)
            z = r * r2 * sin(lat)
            
            # 2 dimensional array index to 1 dimentional
            index = i + j * (total + 1)
            globe[index] = PVector(x, y, z)
    
    offset += 5
    translate(width / 2, height / 2)
    rotateX(angle)
    rotateY(angle)
    rotateZ(angle)
    angle += 0.01
    
    for i in range(total):
        hu = map(i, 0, total, 0, 255 * 6)
        fill((hu + offset) % 255, 255, 255)
        beginShape(TRIANGLE_STRIP)
        
        
        for j in range(total + 1):
            index1 = i + j * (total + 1)
            index2 = (i + 1) + j * (total + 1)
            
            v1 = globe[index1]
            v2 = globe[index2]
            
            vertex(v1.x, v1.y, v1.z)
            vertex(v2.x, v2.y, v2.z)
            
        endShape()
        
