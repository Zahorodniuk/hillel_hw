n = int(input('Enter the number: '))

i = 0
multiple = 1
do = len(str(n))

while i < do:
    multiple = multiple * (n % 10)
    n = int(((n - n % 10) / 10))
    i += 1
    if i == do:
        if multiple > 9:
            n = multiple
            multiple = 1
            i = 0
            do = len(str(n))
print("Results: ", multiple)

