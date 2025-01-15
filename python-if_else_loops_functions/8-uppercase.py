#!/usr/bin/python3
def uppercase(str):
    letter = 0
    new = ""
    while letter < len(str):
        if ord(str[letter]) > 96 and ord(str[letter]) < 123:
            new += chr(ord(str[letter]) - 32)
        else:
            new += str[letter]
        letter += 1
    print("{}".format(new))
