a = int(input())

for i in range(a):
    b = int(input())
    input_list = list(map(int, input()))
    set_list = [0,0,0,0,0,0,0,0,0,0]
    for j in range(b):
        set_list[input_list[j]] += 1

    max_count = max(set_list)
    num_max_count = set_list.count(max_count)

    max_count__value_list = []
    if num_max_count > 1:
        for k in range(num_max_count):
            max_count__value_list.append(set_list.index(max_count))
            set_list[set_list.index(max_count)] -= max_count
        result = max(max_count__value_list)
    
        print(f'#{i+1} {result} {max_count}')
        continue

    else:
        max_value = set_list.index(max_count)


    print(f'#{i+1} {max_value} {max_count}')