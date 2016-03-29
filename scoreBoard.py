#def scoreBoard(b): 
#scoreBoard(b) returns a pair holding the scores for Black and White on board b. 
#e.g. scoreBoard([[0, 1, -3, 1], [-2, 0, 2, -1], [1, 3, 4, -1], [0, -2, -2, 1]]) = (13, 11).




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
