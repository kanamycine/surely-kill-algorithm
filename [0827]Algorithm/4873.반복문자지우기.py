
def solve(input_data):
    stack = []
    for data in input_data:
        if stack == [] or stack [-1] != data:
            stack.append(data)
        elif stack[-1] == data:
            stack.pop()
    return len(stack)

tc = int(input())
for t in range(1, tc+1):
    input_data = input()
    result = solve(input_data)
    print('#{} {}'.format(t, result))

