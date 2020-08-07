tc = int(input())
for t in range(tc):
    arr = [list(map(int, input().split())) for _ in range(9)]

    
    #brd = [0] * 9
    #for i in range(9):
    #   brd[i] = list(map(int, input().split()))


    # arr = [[0]* 9 for _ in range(9)]
    # for i in range(9):
    #     arr[i] = list(map(int, input().split()))
    result = 1
    
    for y in range(9):
        x_sum, y_sum = 0, 0
        for x in range(9):
            x_sum += arr[y][x]
            y_sum += arr[x][y]
    
        if x_sum != 45 or y_sum != 45:
            result = 0
            break

        # 박스검사
        for y in range(3):
            for x in range(3):
                total = 0
                for dy in range(3):
                    for dx in range(3):
                        total += arr[3*y+dy][3*x+dx]

                if total != 45:
                    result = 0
                    break
    
    print('#{} {}'.format(t+1,result))
   

    