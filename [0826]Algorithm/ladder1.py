arr = [[0] * 100 for _ in range(100)]

def check_dir(Y,X):
    if X - 1 > -1 and arr[Y][X - 1] == 1:
        return 2 # 왼쪽
    if X + 1 < 100 and arr[Y][X + 1] == 1:
        return 1 # 오른쪽
    elif Y - 1 > -1 and arr[Y - 1][X] == 1:
        return 0 # 위쪽

def startFind(endX):
    Y, X = 99, endX
    dy = [-1, 0, 0]
    dx = [0, 1, -1]
    while Y > 0:
        arr[Y][X] = -1 #방문한 곳 거르기~
        dir_stat = check_dir(Y, X) 
        Y += dy[dir_stat]
        X += dx[dir_stat]
    return X

for _ in range(10):
    n = int(input())
    endX = 0
    for i in range(100):
        row = list(map(int, input().split()))
        for j in range(100):
            num = row[j]
            if num == 2:
                endX = j
            arr[i][j] = num
    res = startFind(endX)
    print('#{} {}'.format(n, res))