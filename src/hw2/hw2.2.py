number1 = int(input("Введіть 5-ти значне ціле, позитивне число: "))

number_a = number1 // 10000
a = number_a % 100

number_b = number1 // 1000
b = number_b % 10

number_c = number1 // 100
c = number_c % 10

number_d = number1 // 10
d = number_d % 10

number_e = number1 // 1
e = number_e % 10

print(e*10000+d*1000+c*100+b*10+a*1)