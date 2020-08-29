num = int(input())
lst = []
for i in range(num+1):
    lst.append(i)
rvrs = (lst[::-1])

for j in rvrs:
    print(j, end=" ")