
for j in range(10):
    a = int(input())
    input_list = list(map(int, input().split()))

    for i in range(a):

        maxv=max(input_list)
        minv=min(input_list) 

        input_list[input_list.index(maxv)] -= 1 
        input_list[input_list.index(minv)] += 1
    

    print(f'#{j+1} {max(input_list)-min(input_list)}')
        