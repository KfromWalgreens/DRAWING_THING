
rect_count = 5
rect_height = 50
rect_width = 600 / rect_count

def setup(): #runs once
    size(600, 600)
    background(255,255,255)
    rect(0,0,rect_width, rect_height)
    fill(245, 66, 149)
    rect(rect_width ,0,rect_width, rect_height)
    fill(66, 84, 245)
    rect(rect_width*2,0,rect_width, rect_height)
    fill(245, 233, 66)
    rect(rect_width*3,0,rect_width, rect_height)
    fill(84, 245, 66)
    rect(rect_width*4,0,rect_width, rect_height)
    noStroke()
def draw(): #runs multiple times
    if keyPressed and (key == 'c' or key == 'C'):
        background(255,255,255)
    if mousePressed: 
        ellipse(mouseX,mouseY,30,30)
    if (mouseX > rect_width and mouseX < rect_width *2 and mouseY < rect_height and mousePressed):
        fill(245, 66, 149)
        ellipse(mouseX,mouseY,30,30)
    if (mouseX > rect_width *2 and mouseX < rect_width *3 and mouseY < rect_height and mousePressed):
        fill(66, 84, 245)
        ellipse(mouseX,mouseY,30,30)
    if (mouseX > rect_width *3 and mouseX < rect_width *4 and mouseY < rect_height and mousePressed):
        fill(245, 233, 66)
        ellipse(mouseX,mouseY,30,30)
    elif ( mouseX > rect_width *5 and mouseY < rect_height and mousePressed):
        fill(84, 245, 66)
        ellipse(mouseX,mouseY,30,30)

        
    
    
        

    
