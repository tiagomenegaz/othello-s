## 2nd Assignment

#Question 1
#def initialiseBoard(n): 
#initialiseBoard(n) returns the initial board for an Othello game of size n.

def initialiseBoard(n):
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
        
    
