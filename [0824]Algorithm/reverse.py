s = 'iloveyou'
arr = list(s)

for i in range(len(s)//2):
    arr[i], arr[-(i+1)] = arr[-(i+1)], arr[i]

s = ''.join(arr)
print(s)

