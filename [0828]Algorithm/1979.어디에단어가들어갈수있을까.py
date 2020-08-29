tc = int(input())
for t in range(tc):
    N, K = map(int, input().split())

    input_list = [[0] * N for _ in range(N)]

    for a in range(N):
        input_list[a] = list(map(int, input().split()))

    ans = 0
    for b in range(N):
        rowcnt = 0
        colcnt = 0
        for c in range(N):
            if input_list[b][c] == 1:
                rowcnt += 1
            elif input_list[b][c] == 0:
                if rowcnt == K:
                    ans += 1
                rowcnt = 0
            if input_list[c][b] == 1:
                colcnt += 1
            elif input_list[c][b] == 0:
                if colcnt == K:
                    ans += 1
                colcnt = 0
        if rowcnt == K:
            ans += 1
        if colcnt == K:
            ans += 1

    print('#%d %d' % (t+1, ans))
