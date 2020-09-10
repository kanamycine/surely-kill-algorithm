T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    node = [0 for x in range(N+1)]


    for a in range(1, N+1): #123456
        node[a] = arr[a]
        root = a // 2
        while root >= 1:
            if node[a] < node[root]:
                node[a], node[root] = node[root], node[a]
            root = root // 2
            a = a // 2

    result = 0
    root = N // 2
    while root >= 1:
        result += node[root]
        root = root // 2
    print('#{} {}'.format(t,result))