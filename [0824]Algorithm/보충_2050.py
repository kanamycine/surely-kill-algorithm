input_string = input()
number = len(input_string)
result_list = []
for i in input_string:
    val = ord(i) - 64
    result_list.append(val)

for i in result_list:
    print(i, end= " ")