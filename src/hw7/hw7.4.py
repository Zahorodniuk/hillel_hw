from typing import Set


def common_elements():
    r3 = set(range(0, 100, 3))
    r5 = set(range(0, 100, 5))
    is_elements = r3.intersection(r5)

    return is_elements


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('ok')
