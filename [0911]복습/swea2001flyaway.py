tc = int(input())
for t in range(1, tc+1):
    M, N = map(int, input().split())
    arr = [0] * M
    for m in range(M):
        arr[m] = [int(n) for n in input().split()]
    maxsum = 0

    for j in range(M-N+1):
        for k in range(M-N+1):
            tmpsum = 0
            for n in range(N):
                tmpsum += sum(arr[j+n][k:k+N])
            if tmpsum > maxsum:
                maxsum = tmpsum


print(arr)
