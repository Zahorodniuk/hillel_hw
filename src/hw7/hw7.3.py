def second_index(text, some_str):
    out = None
    first_i = text.find(some_str)

    if first_i >= 0:
        second_i = text.find(some_str, first_i + 1)

        if second_i >= 0:
            out = second_i

    return out


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
