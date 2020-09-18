# 길이 입력받기
n = int(input())
lst = [1,2,3]
m = len(lst)

if n == 2:
    for i in range(m):
        for j in range(m):
            print('[{},{}]'.format(lst[i],lst[j]))
    
if n == 3:
    for i in range(m):
        for j in range(m):
            for k in range(m):
                print('[{},{},{}]'.format(lst[i],lst[j],lst[k]))
