def setup(): #runs once
    size(500, 500)
    noStroke()


def draw(): #runs multiple times
    #background(200,200,200)
    if mousePressed: 
        fill(0,128, 128)
        fill(mouseY, mouseX, 90)
        #if mouseX > 250 and mouseY >  250: 
            #fill(66, 135, 245)
        # elif  mouseX < 250 and mouseY >  250: 
        #     fill(245, 66, 87)
        # elif  mouseX > 250 and mouseY <  250: 
        #     fill(59, 217, 20)
        # elif  mouseX < 250 and mouseY <  250: 
        #     fill(238, 255, 0)
        ellipse(mouseX - 50/2,mouseY -50/2,50,50)
    if keyPressed and (key == 'c' or key == 'C'):
        background(200,200,200)
        print(keyCode)

    
