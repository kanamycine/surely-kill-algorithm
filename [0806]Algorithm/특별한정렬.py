T = int(input())
for tc in range(1, T+1):
    b = int(input())
    c = list(map(int, input().split()))
    

    for j in range(b):
        for k in range(j+1, len(c)):
            if j % 2 == 0:
                if c[j] < c[k]:
                    c[j],c[k] = c[k], c[j]
            else: 
                if c[j] > c[k]:
                 c[j],c[k] = c[k],c[j]

    

    print(f'#{tc}', end=' ')
    for z in range(10):
        print(f'{c[z]}', end=' ')
    print()