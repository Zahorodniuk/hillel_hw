make_step = True
while make_step:

    a = float(input("Enter number №1: "))
    oprtr = input("Enter operator (+,-,*,/): ")
    b = float(input("Enter number №2: "))

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

    question = input("Do the math?  [Y/N]")

    if question.lower() == "n":
        make_step = False
        print("End!")
