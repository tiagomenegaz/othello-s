from turtle import Turtle, colormode

def startTurtle():
    t = Turtle()
    t.speed(10)
    t.up()
    t.setpos(-dim/2,-dim/2)
    colormode(255)
    return t

def drawQuare(t):
    t.fillcolor(34,139,34)#GREEN
    t.begin_fill()
    t.down()
    t.forward(dim)
    t.left(90)
    t.forward(dim)
    t.left(90)
    t.forward(dim)
    t.left(90)
    t.forward(dim)
    t.left(90)
    t.end_fill()
    t.up

def drawFrames(t,lines):      
    t.down()

    for i in range(lines):        
        t.forward(scale)
        x = t.xcor()
        y = t.ycor()        
        t.goto(x,y+dim) 
        y = t.ycor() 
        t.goto(x,y-dim)

    t.left(90)   

    for i in range(lines):        
        t.forward(scale)
        x = t.xcor()
        y = t.ycor()        
        t.goto(x-dim,y) 
        x = t.xcor() 
        t.goto(x+dim,y)

    t.up()
    t.setpos(0,0)
    t.setpos(-dim/2,-dim/2)
    t.right(90)

def drawCircle(t,player):
    if(player > 0):
        t.fillcolor(0,0,0)
    else:
        t.fillcolor(255,255,255)

    t.down()
    t.begin_fill()
    t.circle((scale)*0.40)
    t.end_fill()
    t.up()    

def calcMovement(t,x,y):
    x = t.xcor() + x*scale + 0.5*scale
    y = t.ycor() + y*scale + 0.1*scale
    t.setx(x)
    t.sety(y)

def drawValues(t,b):
    xOri = t.xcor()
    yOri = t.ycor()

    for x in range(len(b)):
        for y in range(len(b)):
            if(b[y][x] > 0):
                calcMovement(t,x,y)
                drawCircle(t,1)
            elif (b[y][x] < 0):
                calcMovement(t,x,y)
                drawCircle(t,-1)
            t.goto(xOri,yOri)    

    t.up()
    
def drawBoard(b):
    global scale
    global dim    
    scale = 100
    dim   = scale * len(b)
    
    t = startTurtle()
    drawQuare(t)
    drawFrames(t,len(b))
    drawValues(t,b)
    
