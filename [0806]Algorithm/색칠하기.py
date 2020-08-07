a = int(input())
for i in range(a):
    b = int(input())
    arr = [[0] * 10 for _ in range(10)]
    for j in range(b):
        inputlist = []
        inputlist = list(map(int, input().split()))
        
        for l in range(inputlist[0]  , inputlist[2] + 1 ):
            for k in  range(inputlist[1] , inputlist[3] + 1 ):
                arr[l][k] += inputlist[4]
    cnt = 0
    for m in arr:
        cnt += m.count(3)

    print(f'#{i + 1} {cnt}')