import random
input_list = [random.randint(3,10) for i in range(random.randint(3, 10))]
print(input_list)

new_list = [input_list[0], input_list[2], input_list[-2]]
print(new_list)