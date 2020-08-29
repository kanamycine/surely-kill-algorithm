a = int(input())

for i in range(a):
    a, b = map(int, input().split())
    x = a // b
    y = a % b
    print('#{} {}'.format(x,y))