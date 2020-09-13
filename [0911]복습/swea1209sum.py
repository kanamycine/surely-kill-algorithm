for _ in range(10):
    tn = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]

    total = []
    tmp = 0
    for i in range(100):
        total.append(sum(arr[i]))

    for i in range(100):
        for j in range(100):
            tmp += arr[i][j]
        total.append(tmp)
        tmp = 0

    for i in range(100):
        tmp += arr[i][i]
        total.append(tmp)
        tmp = 0

    for i in range(100):
        for j in range(99, 0, -1):
            tmp += arr[i][j]
        total.append(tmp)
        tmp = 0

    print(max(total))
