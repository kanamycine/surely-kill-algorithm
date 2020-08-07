# 가로축 길이 체크
def width(i,j):
    cnt = 1
    dx = j
    while True:
        dx += 1
        if dx >= N:
            break
        if arr[i][dx]:
            cnt += 1
        else:
            break
    return cnt

# 세로축 길이 체크
def height(i,j):
    cnt = 1
    dy = i
    while True:
        dy += 1
        if dy >= N:
            break
        if arr[dy][j]: 
            cnt += 1
        else:
            break
    return cnt

# 이미 검사한 곳은 0으로 바꿔주는 놈
def change_zero(sy, sx, ey, ex):
    for i in range(sy, ey):
        for j in range(sx, ex):
            arr[i][j] = 0

T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = []
    for  i in range(N):
        for j in range(N):

            #값이 있을때
            if arr[i][j]:
                #가로 세로 길이를 받아서
                w = width(i, j)
                h = height(i, j)
                #리스트 중 검사된 애들 0으로 변경
                change_zero(i,j, i+h, j+w)
                #행렬 크기 넣고 곱한 값 넣고,
                result.append([h*w ,h, w])
    # 출력을 위한 정렬 
    result.sort()

    print('#{} {}'.format (t, len(result)), end = ' ')
    for _, r, c in result:
        print('{} {}'.format(r,c), end= ' ')
    print()
