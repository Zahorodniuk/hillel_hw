a = float(input("Enter number №1: "))
oprtr = input("Enter operator (+,-,*,/): ")
b = float(input("Enter number №2: "))
9
if oprtr == '+':
    result = a + b
    print(result)

elif oprtr == '-':
    result = a - b
    print(result)

elif oprtr == '*':
    result = a * b
    print(result)

elif oprtr == '/':
    if b != 0:
        result = a / b
        print(result)
    else:
        print('Immposible to devide by 0')
else:
    print('Error')