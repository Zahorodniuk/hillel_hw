def say_hi(name, age):
    say = f"Hi. My name is {str(name)} and I'm {int(age)} years old"
    return say


assert say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old", 'Test1'
assert say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old", 'Test2'
print('ОК')