import re


def is_palindrome(data):
    data = re.sub('[.,:;?!]', '', data)
    data = data.replace(' ', '').lower()

    return data == data[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') is True, 'Test1'
assert is_palindrome('0P') is False, 'Test2'
assert is_palindrome('a.') is True, 'Test3'
assert is_palindrome('aurora') is False, 'Test4'
print("ОК")
