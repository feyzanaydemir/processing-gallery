axiom = "F"
sentence = axiom
rules = [{"start": "F", "end": "FF+[+F-F-F]-[-F+F+F]"}]
angle = radians(25)
len = 150
depth = 0

def trace():
    global len
    resetMatrix()
    background(30)
    stroke(255, 100)
    translate(width / 2, height)
    
    len *= 0.57
    
    for char in sentence:
        if char == "F":
            line(0, 0, 0, -len)
            translate(0, -len)
        elif char == "+":
            rotate(angle)
        elif char == "-":
            rotate(-angle)
        elif char =="[":
            push()
        elif char == "]":
            pop()


def generate():
    global sentence
    next_sentence = ""
    
    for char in sentence:
        is_rule_found = False
        
        for rule in rules:
            if char == rule["start"]:
                next_sentence += rule["end"]
                is_rule_found = True
                break
            
        if not is_rule_found:
            next_sentence += char
    
    sentence = next_sentence
    trace()
    
    
def setup():
    size(600, 600)
    trace()
    
    
def draw():
    global depth, sentence, len
    if mousePressed:
        depth += 1
        
        if depth > 5:
            sentence = axiom
            depth = 0
            len = 100 * 0.57
        
        generate()
