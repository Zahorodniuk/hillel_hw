input_list = [0, 1, 0, 12, 3]
# input_list = [0]
# input_list = [1, 0, 13, 0, 0, 0, 5]
# input_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

n = len(input_list)
zero = 0

for i in range(n):
    if input_list[i] != 0:
        input_list[zero], input_list[i] = input_list[i], input_list[zero]
        zero += 1

print(input_list)