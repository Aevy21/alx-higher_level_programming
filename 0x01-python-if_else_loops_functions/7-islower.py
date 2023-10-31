#!/usr/bin/python3
def islower(c):
    for char in c:
        if not 'a' <= char <= 'z':
            return False
    return True
