tc = int(input())

for t in range(1, tc+1):
    N,M = map(int,input().split())
    result = []
    
    in_put = []
    for _ in range(N):
        in_put.append(input())
    #x축
    for r in range(N):
        for c in range(N-M+1):
            if in_put[r][c:c+M] == in_put[r][c:c+M][::-1]:
                result.append(in_put[r][c:c+M])
    
    #y축
    for r in range(N-M+1):
        for c in range(N):
            column_list =[]
            for i in range(M):
                column_list.append(in_put[r+i][c])
            if column_list == column_list[::-1]:
                result.append(''.join(column_list))
    
    print('#{} {}'.format(t, result[0]))