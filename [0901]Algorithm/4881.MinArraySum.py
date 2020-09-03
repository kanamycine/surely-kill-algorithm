def MyCalc(y):
    global sub_total, total

    if total < sub_total:
        return

    if y == N:
        if sub_total < total:
            total = sub_total
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = True
            sub_total += lst[y][x]
            MyCalc(y+1)
            visited[x] = False
            sub_total -= lst[y][x]


TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    sub_total, total = 0, 987654321
    MyCalc(0)

    print(f'#{tc} {total}')