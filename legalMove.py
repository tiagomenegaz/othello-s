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

def legalMove(r,c,b,p):
    legalMoveList = []
    for v in (-1,0,1):
        for u in (-1,0,1):
            if (u != 0 or v != 0) and legalDirection(r,c,b,p,u,v):
                legalMoveList.append((u,v))
    return legalMoveList

def moves(b, p):
    movesList = []
    for c in range(len(b)):
        for r in range(len(b)):
            if legalMove(r,c,b,p) != []:
                movesList.append((r,c,legalMove(r,c,b,p)))
    return movesList

def selectMove(ms,b,p):
    return ms[random.randint(0,len(b)-1)]
