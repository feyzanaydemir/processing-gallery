# phi = n + 137.5deg
# r = c + sqrt(n)

# number of dots
n = 0
c = 5

def setup():
    size(400, 400)
    background(10)
    colorMode(HSB)


def draw():
    global n
    
    if n < 1000:
        phi = n * 137.3
        r = c * sqrt(n)
        x = r * cos(phi) + width / 2
        y = r * sin(phi) + height / 2
        
        fill(n % 255, 255, 255)
        circle(x, y, 8)
        n += 1
        
