
#def move(b, m, p): 
#move(b, m, p) updates the board b with all effects of the move m by player p, and it also updates the screen accordingly. 
#e.g. move([[2, -1, 0, 0], [0, -3, -2, -1], [0, 0, -1, 0], [0, -1, 2, 0]], (0, 2, [(1, 0), (0, -1)]), 1) returns 
#[[2, 2, 1, 0], [0, -3, 3, -1], [0, 0, 2, 0], [0, -1, 2, 0]], and it updates on the display all squares that have changed colour.

def move(b,m,p): #for a legal move, ms will not be [ ]. Checking it??
    x=m[0]
    y=m[1]
    if p >0: # Black case
        for i in range(len(m[2])):
            while b[x][y] < p:
                b[x][y] = abs(b[x][y]) + p
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
                b[m[0]][m[1]] = 0
                x += m[2][i][0]
                y += m[2][i][1]
            x=m[0]
            y=m[1]
        b[m[0]][m[1]] = -1
        return b

    
        
