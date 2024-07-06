test_input_1 = [1, 2, 3, 4, 5, 6]
test_input_2 = [1, 2, 3]
test_input_3 = [1, 2, 3, 4, 5]
test_input_4 = [1]
test_input_5 = []

input_list = test_input_1

size = len(input_list)
i = size - size // 2

result = [input_list[:i], input_list[i:]]
print(result)

