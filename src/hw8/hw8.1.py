
def add_one(some_list):
    str_value_before_incr = str(some_list)[1:-1].replace(", ", "")
    incr_value = int(str_value_before_incr) + 1
    str_value_after_incr = str(incr_value)

    return [int(i) for i in list(str_value_after_incr)]


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")


