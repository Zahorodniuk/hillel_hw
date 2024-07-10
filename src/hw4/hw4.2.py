input_list = [0, 1, 7, 2, 4, 8]
# input_list = [1, 3, 5]
# input_list = [6]
# input_list = []

if len(input_list) == 0:
    print(0)
else:
    b = input_list[::2]
    final = sum(b) * input_list[-1]
    print(final)
