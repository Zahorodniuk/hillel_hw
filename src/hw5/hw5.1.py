import keyword

name = input("Enter the name: ")

if name.isidentifier() \
        and name.count("__") == 0 \
        and name not in keyword.kwlist \
        and name == name.lower():
    print(True)
else:
    print(False)
