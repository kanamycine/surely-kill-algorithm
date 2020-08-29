tc = int(input())

for t in range(1, tc+1):
    input_1 = input()
    input_2 = input()

    result = 0 
    for i in range(len(input_2)-len(input_1) + 1):
        if input_2[i:i+len(input_1)]== input_1:
            result = 1
    print('#{} {}'.format(t, result))