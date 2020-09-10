def inorder(node):
    global cnt
    if node == 0:
        return
    cnt += 1
    inorder(left[node])
    inorder(right[node])


tc = int(input())
for t in range(1, tc + 1):
    E , N = map(int,input().split())
    arr = list(map(int,input().split()))

    left = [0] * (E+2)
    right = [0] * (E+2)

    for i in range(0,len(arr),2):
        parent, son = arr[i], arr[i+1]
        if left[parent]:
            right[parent] = son
        else:
            left[parent] = son

    cnt = 0
    inorder(N)
    print('#{} {}'.format(t, cnt))