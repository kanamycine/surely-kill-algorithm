
dr =[-1, 1, 0 ,0]
dc = [0, 0, -1, 1]

def bfs(r, c):
    queue = [(r,c)]
    dist[r][c] = 0

    while len(queue) > 0:
        row, col = queue.pop(0)
        #arrival
        if maze[row][col] =='3':
            break

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            #boundary value setting
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # not visit yet, not wall
            if maze[nr][nc] != '1' and dist[nr][nc] == 987654321:
                dist[nr][nc] = dist[row][col] + 1
                queue.append((nr,nc))

tc = int(input())
for t in range(1, tc+1):
    N = int(input())
    maze = [list(input()) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            #starting point
            if maze[i][j] == '2':
                sR = i
                sC =j
            #end point
            if maze[i][j] == '3':
                eR = i
                eC = j
    
    dist = [[987654321] * N for _ in range(N)]
    bfs(sR,sC)

    if dist[eR][eC] == 987654321:
        dist[eR][eC] = 1
    print('#{} {}'.format(t, dist[eR][eC] - 1 ))