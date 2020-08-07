a = int(input())
for i in range(a):
    b = int(input())
    input_list = list(map(int, input().split()))
    min_value = input_list[0]
    max_value = input_list[0]
    #max
    for j in range(b):
        if input_list[j] > max_value:
            max_value = input_list[j]
    #min
    for k in range(b):
        if input_list[k] < min_value:
            min_value = input_list[k]

    result = max_value - min_value

    print(f'#{i + 1} {result}')