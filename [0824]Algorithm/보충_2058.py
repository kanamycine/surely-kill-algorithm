a = int(input())

for i in range(a):
    b = list(map(int,input().split()))
    max_num = b[0]
    for j in range(len(b)):
        if max_num <= b[j]:
            max_num = b[j]
        else :
            continue
    print(f'#{i+1} {max_num}')
