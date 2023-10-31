#!/usr/bin/python3

for characters in range(97, 123):
    if chr(characters) not in ('q', 's'):
        print("{}".format(chr(characters)), end='')
