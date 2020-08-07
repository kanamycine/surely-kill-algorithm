a = int(input())
for i in range(a):
    N, M = map(int, input().split())
    
    arr = [0] * N
    for n in range(N):
        arr[n] = [int(n) for n in input().split()]
    maxsum=0
    for j in range(N-M+1):
        for k in range(N-M+1):
            tmpsum=0
            for m in range(M):
                tmpsum += sum(arr[j+m][k:k+M])
            if tmpsum > maxsum:
                maxsum = tmpsum

    print('#%d %d' % (i+1, maxsum))