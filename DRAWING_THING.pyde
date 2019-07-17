import random
rect_count = 5
rect_height = 50
rect_width = 800 / rect_count
a = color(10, 10, 10)
b = color(245, 245, 245)
# c = color(50, 55, 100)
# colors = [a,b,c]

def setup(): #runs once
    size(800, 800)
    background(255,255,255)
    fill(255,255,255)
    rect(0,0,rect_width, rect_height)
    fill(245, 66, 149)
    rect(rect_width ,0,rect_width, rect_height)
    fill(66, 84, 245)
    rect(rect_width*2,0,rect_width, rect_height)
    fill(245, 233, 66)
    rect(rect_width*3,0,rect_width, rect_height)
    fill(255,255,255)
    rect(rect_width*4,0,rect_width, rect_height)
    noStroke()
def draw(): #runs multiple times
    textSize(20)
    text("Eraser", 50, 30)
    if keyPressed and (key == 'c' or key == 'C'):
        background(255,255,255)
    if mousePressed and mouseY > rect_height + 20 and mouseX : 
        ellipse(mouseX,mouseY,30,30)
    if (mouseX < rect_width and mouseY < rect_height and mousePressed):
        fill(255,255,255)
    elif (mouseX > rect_width and mouseX < rect_width *2 and mouseY < rect_height and mousePressed):
        fill(245, 66, 149)
    elif (mouseX > rect_width *2 and mouseX < rect_width *3 and mouseY < rect_height and mousePressed):
        fill(66, 84, 245)
    elif (mouseX > rect_width *3 and mouseX < rect_width *4 and mouseY < rect_height and mousePressed):
        fill(245, 233, 66)
    elif ( mouseX > rect_width *4 and mouseY < rect_height and mousePressed):
        fill(random.choice(range(a,b)))
    textSize(20)
    text("RaNdOm", 660, 30)


        
    
    
        

    
