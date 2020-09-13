for t in range(1, 11):
    dump = int(input())
    lst = list(map(int, input().split()))

    for i in range(dump):
        maxv = max(lst)
        minv = min(lst)

        lst[lst.index(maxv)] -= 1
        lst[lst.index(minv)] += 1
    print('#{} {}'.format(t, max(lst)-min(lst)))