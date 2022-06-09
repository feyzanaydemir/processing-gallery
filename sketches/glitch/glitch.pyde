org, sorted_alpha, sorted_hue, sorted_satur = None, None, None, None

def create_sample(start, end, img):
    sample = []
    
    for i in range(start, end):
        sample.append(img.pixels[i])
        
    return sample


def fill_sample(start, sample, img):
    for i in range(start, len(sample)):
        img.pixels[i], sample[i] = sample[i], img.pixels[i]
        
    return img


def setup():
    global org, sorted_alpha, sorted_hue, sorted_satur
    org = loadImage("girl_with_a_pearl_earring.jpg")
    org.resize(450, 345)
    size(900, 690)
    
    sorted_alpha = org.get()
    sorted_hue = org.get()
    sorted_satur = org.get()
    
    sorted_alpha.loadPixels()
    sorted_hue.loadPixels()
    sorted_satur.loadPixels()
    
    sample_alpha = create_sample(2000, 69000, sorted_alpha)
    sample_hue = create_sample(0, len(sorted_hue.pixels), sorted_hue)
    sample_satur = create_sample(0, len(sorted_satur.pixels), sorted_satur)    
    
    sample_alpha.sort(key=lambda px: alpha(px))
    sample_hue.sort(key=lambda px: hue(px))
    sample_satur.sort(key=lambda px: saturation(px))
        
    sorted_alpha = fill_sample(20000, sample_alpha, sorted_alpha)
    sorted_hue = fill_sample(0, sample_hue, sorted_hue)
    sorted_satur = fill_sample(0, sample_satur, sorted_satur)

    sorted_alpha.updatePixels()
    sorted_hue.updatePixels()
    sorted_satur.updatePixels()
  

def draw():
    background(0)
    image(org, 0, 0)
    image(sorted_alpha, width/2, 0)
    image(sorted_hue, 0, height/2)
    image(sorted_satur, width/2, height/2)
    
