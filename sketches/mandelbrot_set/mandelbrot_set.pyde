def setup():
    size(640, 360)
    colorMode(HSB)
    noLoop()


def draw():
    background(255)
    
    w = float(4)
    h = (w * height) / width

    x_min = -w / 2
    y_min = -h / 2
    x_max = x_min + w
    y_max = y_min + h
    dx = (x_max - x_min) / width
    dy = (y_max - y_min) / height
    
    max_iterations = 100
    
    loadPixels()

    y = y_min
    
    for j in range(height):
        x = x_min
        
        for i in range(width):
            a = x
            b = y
            n = 0
            max = float(16)
            abs_prev = float(0)
            converge = max_iterations
            
            while (n < max_iterations):
                abs = sqrt(a ** 2 + b ** 2)
                
                if abs > max:
                    delta_last = abs - abs_prev
                    delta_max = max - abs_prev
                    converge = n + delta_max / delta_last
                    break
                
                abs_prev = abs
                two_ab = 2 * a * b
                a = a ** 2 - b ** 2 + x
                b = two_ab + y
                n += 1
                
            if n == max_iterations:
                pixels[i + j * width] = color(100, 50, 255)
            else:
                norm = map(converge, 0, max_iterations, 0, 1)
                hu = map(sqrt(norm), 0, 1, 0, 255)
                pixels[i + j * width] = color(255-hu, 255-hu, 255)
            
            x += dx
            
        y += dy
    
    updatePixels()
