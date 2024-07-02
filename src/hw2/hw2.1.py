number1 = int(input("Введіть 4-х значне число:"))

number_a = number1 // 1000
a = number_a % 100

number_b = number1 // 100
b = number_b % 10

number_c = number1 // 10
c = number_c % 10

number_d = number1 // 1
d = number_d % 10

print(a)
print(b)
print(c)
print(d)