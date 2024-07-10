input_list = [0, 1, 0, 12, 3]
# input_list  = [0]
# input_list  = [1, 0, 13, 0, 0, 0, 5]
# input_list  = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

result_list = []

for i in input_list:
    if i != 0:
        result_list.append(i);

zero_number = len(input_list) - len(result_list)

for i in range(zero_number):
    result_list.append(0)

if len(input_list) == len(result_list):
    print(result_list)