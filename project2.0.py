## 2nd Assignment

#Question 1
#def initialiseBoard(n): 
#initialiseBoard(n) returns the initial board for an Othello game of size n.

from turtle import Turtle, colormode
import random

#1 --------------------------------------------------------------------------------------------------------------####
def initialiseBoard(n):
    if n % 2 == 1:
        print("ERROR: Board size has to be even")
        return []
    zeros = [0]*n
    for i in range(0,n):
        zeros[i]=[0]*n
    pos2 = int(len(zeros)/2) #Position 4
    pos = int(pos2-1) #From example -> Position 3
    zeros[pos][pos] = 1
    zeros[pos][pos2] = -1
    zeros[pos2][pos] = -1
    zeros[pos2][pos2] = 1
    return zeros        
    
#2 --------------------------------------------------------------------------------------------------------------####
def startTurtle():
    t = Turtle()
    t.hideturtle()
    t.speed(10)
    t.up()
    t.setpos(-dim/2,-dim/2)
    colormode(255)
    return t

def drawSquare():
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

def drawFrames(lines):      
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

def drawCircle(player):
    if(player > 0):
        t.fillcolor(0,0,0)
    else:
        t.fillcolor(255,255,255)

    t.down()
    t.begin_fill()
    t.circle((scale)*0.40)
    t.end_fill()
    t.up()    

def calcMovement(x,y):
    x = t.xcor() + x*scale + 0.5*scale
    y = t.ycor() + y*scale + 0.1*scale
    t.setx(x)
    t.sety(y)

def drawValues(b):
    xOri = t.xcor()
    yOri = t.ycor()

    for x in range(len(b)):
        for y in range(len(b)):
            if(b[y][x] > 0):
                drawMovement(x,y,1)
            elif (b[y][x] < 0):
                drawMovement(x,y,-1) 

    t.up()
    
def drawBoard(b):
    global scale
    global dim 
    global t   
    scale = 100
    dim   = scale * len(b)
    
    t = startTurtle()
    drawSquare()
    drawFrames(len(b))
    drawValues(b)

#3 --------------------------------------------------------------------------------------------------------------####

def drawMovement(x,y,p):
    xOri = t.xcor()
    yOri = t.ycor()
    calcMovement(x,y)
    drawCircle(p)
    t.goto(xOri,yOri)


def move(b,m,p): #for a legal move, ms will not be [ ]. Checking it??
    x=m[0]
    y=m[1]
    if p >0: # Black case
        for i in range(len(m[2])):
            while b[x][y] < p:
                b[x][y] = abs(b[x][y]) + p                
                drawMovement(y,x,p)
                b[m[0]][m[1]]= 0
                x += m[2][i][0]
                y += m[2][i][1]
            x=m[0]
            y=m[1]
        b[m[0]][m[1]] = 1
        return b    
    else:    # White case    
        for i in range(len(m[2])):
            while b[x][y] > p:
                b[x][y] = -abs(b[x][y]) + p
                drawMovement(y,x,p)
                b[m[0]][m[1]] = 0
                x += m[2][i][0]
                y += m[2][i][1]
            x=m[0]
            y=m[1]
        b[m[0]][m[1]] = -1
        return b

#4 --------------------------------------------------------------------------------------------------------------####
def legalDirection(r, c, b, p, u, v):
    legalDir = False
    legalInv = False
    if b[r][c] != 0:
        return legalDir
    r += u
    c += v
    times = 0
    while (0 <= r and r < len(b)) and (0 <= c and c < len(b)):
        times += 1
        if p == 1:
            if b[r][c] < 0:
                legalDir = True
            elif b[r][c] == 0:
                legalDir = False
                break
            else:
                legalInv = True
                break
        else:
            if b[r][c] > 0: #Before, I did b[r][c]>p
                legalDir = True
            elif b[r][c] == 0 :
                legalDir = False    
                break    
            else:
                legalInv = True
                break
        r += u
        c += v
        
    if times < 2:
        return False
    return legalDir and legalInv

#5 --------------------------------------------------------------------------------------------------------------####
def legalMove(r,c,b,p):
    legalMoveList = []
    for v in (-1,0,1):
        for u in (-1,0,1):
            if (u != 0 or v != 0) and legalDirection(r,c,b,p,u,v):
                legalMoveList.append((u,v))
    return legalMoveList
        
#6 --------------------------------------------------------------------------------------------------------------####
def moves(b, p):
    movesList = []
    for c in range(len(b)):
        for r in range(len(b)):
            if legalMove(r,c,b,p) != []:
                movesList.append((r,c,legalMove(r,c,b,p)))
    return movesList

#7 --------------------------------------------------------------------------------------------------------------####
def selectMove(ms,b,p):
    return ms[random.randint(0,len(ms)-1)]

        
def selectHighestScoreMove(m,b,p):
    return []
#8 --------------------------------------------------------------------------------------------------------------####
def scoreBoard(b):
    white = 0
    black = 0
    for i in range(len(b)):
        for j in range(len(b[i])):
            if b[i][j]>0:
                black = black + abs(b[i][j])
            elif b[i][j]<0: 
                white = white + abs(b[i][j]) #IF b[i][j]==0, I haven't done anything yet
    return (black,white)
#9 --------------------------------------------------------------------------------------------------------------####

def humPC():
    size = int(input("Enter a even number for the table size: "))
    b = initialiseBoard(size)
    if b != []:
        drawBoard(b)
        print("You are Black player and playing against Computer")
        msb = moves(b,1)
        msw = moves(b,-1)
        while(msb != [] or msw != []):
            print(msb)
            if len(msb) > 0:
                s = "Please select your next movement: [0 up to " + str(len(msb)-1) + "]"
                movement = int(input(s))
                move(b,msb[movement],1)
            else:
                print("You do not have any movements left. Wait your next turn")                    

            msw = moves(b,-1)
            if len(msw) > 0:
                m  = selectMove(msw,b,-1)
                move(b,m,-1)

            msb = moves(b,1)
        print("----------------")
        print("Game has finished")
        print("Your score:  ",scoreBoard(b)[0])
        print("Enemy score: ",scoreBoard(b)[1])
        if scoreBoard(b)[0] > scoreBoard(b)[1]:
            print("You won the game!!!")
        elif scoreBoard(b)[0] == scoreBoard(b)[1]:
            print("The game was a drawn")
        else:
            print("Try again")

def pcPC():
    size = int(input("Enter a even number for the table size: "))
    b = initialiseBoard(size)
    if b != []:
        drawBoard(b)
        msb = moves(b,1)
        msw = moves(b,-1)
        while(msb != [] or msw != []):
            if len(msb) > 0:
                m = selectMove(msb,b,1)
                move(b,m,1)
            else:
                print("You do not have any movements left. Wait your next turn")
            msw = moves(b,-1)
            if len(msw) > 0:
                movement  = selectMove(msw,b,-1)
                move(b,movement,-1)

            msb = moves(b,1)
        print("----------------")
        print("Game has finished")
        print("Black score: ",scoreBoard(b)[0])
        print("White score: ",scoreBoard(b)[1])
        if scoreBoard(b)[0] > scoreBoard(b)[1]:
            print("Black won the game")
        elif scoreBoard(b)[0] == scoreBoard(b)[1]:
            print("The game was a drawn")
        else:
            print("White won the game")
        
def main():
    print("----------------\n")
    print("Authors\nGuilherme Silva - 21364371\nTiago Garcia - 21260915")
    print("Version: 1.0")
    print()
    print("----------------")
    print("Game of Othello")
    print("----------------\n")
    choice = int(input("Press 1 for Humam vs Computer\nPress 2 for Computer vs Computer\n"))
    if choice == 1:
        humPC()
    elif choice == 2:
        pcPC()
    else:
        print("ERROR: You should have entered the number 1 (For playing against computer) or number 2 (For watch the match between computers")
main()
