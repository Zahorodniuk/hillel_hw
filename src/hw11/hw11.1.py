from inspect import isgenerator


def prime_generator(end):
    lst = {}
    num = 2
    while num <= end:
        if num not in lst:
            yield num
            lst[num ** 2] = [num]
        else:
            for i in lst[num]:
                lst.setdefault(i + num, []).append(i)
        num += 1


gen = prime_generator(1)

assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')