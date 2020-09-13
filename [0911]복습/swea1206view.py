for t in range(10):
    n = int(input())
    lst = list(map(int, input().split()))
    cnt = 0
    for i in range(2, n-2):
        if lst[i] > lst[i-1]:
            if lst[i] > lst[i-2]:
                if lst[i] > lst[i+1]:
                    if lst[i] > lst[i+2]:
                        cnt += lst[i] - \
                            max(lst[i-1], lst[i-2], lst[i+1], lst[i+2])
    print('#{} {}'.format(t+1, cnt))
