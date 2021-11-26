def is_palindrome(string):
    return string.lower() == string[::-1].lower()

print(is_palindrome("poP"))

import string

def is_palindrome_s(str):
    whitelist = set(string.ascii_lowercase)
    str = str.lower()
    str = ''.join([char for char in str if char in whitelist])
    return str == str[::-1]

print(is_palindrome_s('A dog! A panic in a pagoda'))