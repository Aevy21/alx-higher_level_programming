#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            # Convert lowercase letter to uppercase by shifting ASCII value
            uppercase_char = chr(ord(char) - 32)
            result += uppercase_char
        else:
            result += char
    print(result)
