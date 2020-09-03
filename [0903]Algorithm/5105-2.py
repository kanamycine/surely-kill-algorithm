def BFS(stX, stY):
    Q = []
    dx = []
    dy = []

    Q.append((stX, stY))
    BRD[stY][stX] = -1

    while Q:
        curX,  curY = Q.pop(0)
        for i in range(4):
            newX = curX + dx[i]
            newY = curY + dy[i]
            
            if BRD[newY][newX] == 0 #and BRD[newY][newX] != -1:
                Q.append((newX, newY))
                BRD[newY][newX] = -1

    return 0






T = int(input())
for tc in range(1, T+1):
    N = int(input())

    #1

    BRD = [input() for _ in range(N)]
    '''
    for i in range(N):
        for j in range(N):
            if BRD[i][j] = '2'
                stX =j
                stJ =i
                break
    '''
    for i in range(N):
        if BRD[i].count('2') > 0:
            stX = BRD[i].index('2')
            stY = i
            break

    #2
    BRD = [[] for _ in range(N)]
    for i in range(N):
        BRD[i] = input()
    print(BRD)
