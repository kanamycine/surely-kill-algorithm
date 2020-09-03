tc = int(input())
for tc in range(1, tc+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for i in range(M):
        p = lst.pop(0)
        lst.append(p)
    
    print('#{} {}'.format(tc, lst[0]))

