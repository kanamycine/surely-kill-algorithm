for t in range(1, 11):
    tc = int(input())
    N = 100
    result = 1
    
    x_list = []
    for i in range(N):
        input_data = input()
        x_list.append(input_data)

        for M in range(N, result, -1):
            if result > M:
                break
            for k in range(N-M+1):
                if input_data[k:M+k] == input_data[k:M+k][::-1]:
                    if len(input_data[k:M+k]) > result:
                        result = len(input_data[k:M+k])

    y_list = []
    y_sub_list = ''
    for x in range(N):
        for y in x_list:
            y_sub_list += y[x]
        y_list.append(y_sub_list)
        y_sub_list = ''

    for y_data in y_list:
        for M in range(N, result, -1):
            if result > M :
                break
            for k in range(N-M+1):
                if y_data[k:M+k] == y_data[k:M+k][::-1]:
                    result = len(y_data[k:M+k])
                    
    print("#{} {}".format(tc, result))
