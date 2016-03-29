def legalDirection(r, c, b, p, u, v):
    legalD = False
    if b[r][c] != 0:
        return legalD
    r += u
    c += v
    while (0 <= r and r < len(b)) and (0 <= c and c < len(b)):
        if p == 1:
            if b[r][c] < 0:
                legalD = True
            if b[r][c] >= p:
                break
        else:
            if b[r][c] > 0: #Before, I did b[r][c]>p
                legalD = True
            if b[r][c] <= p:
                break
        r += u
        c += v
    return legalD
