from string import ascii_letters

a, b, c = input('Enter two letters separated by a hyphen: ')

print(ascii_letters[ascii_letters.index(a):ascii_letters.index(c) + 1])