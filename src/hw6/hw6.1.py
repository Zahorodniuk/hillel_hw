from string import ascii_letters

ascii_range = input('Enter two letters separated by a hyphen: ')


print(ascii_letters[ascii_letters.index(ascii_range[0]):ascii_letters.index(ascii_range[2]) + 1])
