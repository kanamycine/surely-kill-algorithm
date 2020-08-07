a = int(input())
for i in range(a):
    length_list, section_size = map(int, input().split()) 
    input_list = list(map(int, input().split()))
    
    sums_list = []
    for j in range(length_list - section_size + 1):
        sums_list.append(sum(input_list[j:j+section_size]))
    
    result = max(sums_list) - min(sums_list)

    print(f'#{i+1} {result}')