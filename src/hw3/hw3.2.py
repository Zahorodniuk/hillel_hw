testinput1 = [12, 3, 4, 10]
testinput2 = [1]
testinput3 = []
testinput4 = [12, 3, 4, 10, 8]

input_list = testinput4
list_len = len(input_list)

if list_len > 1:
    x = input_list.pop(list_len - 1)
    input_list.insert(0, x)

print(input_list)