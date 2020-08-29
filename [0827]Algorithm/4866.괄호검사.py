tc = int(input())
for t in range(1, tc+1):
    data = input()
    N = len(data)
    stack = []
    for i in range(N):
        if data[i] == "(" or data[i] == "{":
            stack.append(data[i])
        elif data[i] == ")" or data[i] == "}":
            if len(stack) == 0:
                stack = [data[i]]
                break
            elif (data[i] == "}" and stack[-1] != "{") or (data[i] == ")" and stack [-1] != "("):
                stack = [data[i]]
                break
            else: 
                stack.pop()

    if not len(stack):
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))