import keyword


def check(name):
    if name.isidentifier() \
            and name.count("__") == 0 \
            and name not in keyword.kwlist \
            and name == name.lower():
        return True
    else:
        return False


assert_map = {
    "_": True,
    "__": False,
    "___": False,
    "x": True,
    "get_value": True,
    "get value": False,
    "get!value": False,
    "some_super_puper_value": True,
    "Get_value": False,
    "get_Value": False,
    "getValue": False,
    "3m": False,
    "m3": True,
    "assert": False,
    "assert_exception": True
}


for k, v in assert_map.items():
    if check(k) == v:
        print("All right")
    else:
        print("Wrong")

