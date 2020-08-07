def binarySearch(p, target):
    start = 1
    mid = (start + p) // 2
    cnt = 0

    while mid != target:

        if mid == target:
            return mid
        if mid < target:
            start = mid
        else:
            p = mid
        mid = (start+p)//2
        cnt += 1
        
    return cnt



a = int(input())
for i in range(a):
    P, A, B = map(int, input().split())

    #바이너리 서치

    result = 0 

    if binarySearch(P, A) == binarySearch(P, B):   
        result = 0

    if binarySearch(P, A) > binarySearch(P, B):
        result = "B"
    
    if binarySearch(P, A) < binarySearch(P, B):
        result = "A"

    print(f'#{i+1} {result}')