dx = (0, 0, -1, 1)
dy = (-1, 1, 0, 0)

def DFS(y, x, s):
    global result
    if len(s) == 7:
        result.add(s)
        return
    for d in range(4):
        ny, nx = y + dy[d], x + dx[d]
        if 0 <= ny < 4 and 0 <= nx < 4:
            DFS(ny, nx, s + MAP[ny][nx])

T = int(input())
for test_case in range(1, 1 + T):
    MAP = [list(input().split()) for _ in range(4)]
    result = set()
    for r in range(4):
        for c in range(4):
            DFS(r, c, MAP[r][c])
    print('#{} {}'.format(test_case, len(result)))
