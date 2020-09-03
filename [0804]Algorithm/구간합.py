a = int(input())
for i in range(a):
    length_list, section_size = map(int, input().split()) 
    input_list = list(map(int, input().split()))
    
    sums_list = []
    for j in range(length_list - section_size + 1):
        sums_list.append(sum(input_list[j:j+section_size]))
    
    result = max(sums_list) - min(sums_list)

    print(f'#{i+1} {result}')



# arr = [3,6,7,1,5,4]
# n = len(arr) # : 원소의개수

# for i in range(1<<n): #2**n 부분 집합의 개수
#     for j in range(n+1): 원소의 수만큼 비트를 비교
#         if i & (1<<j): i의 j번째 비트가 1이면 j번째 원소 출력
#             print(arr[j], end=",")