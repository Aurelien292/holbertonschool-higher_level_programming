#!/usr/bin/python3
Index = 0
for char in range(ord('z'), ord('a')-1, -1):
    print("{}".format(chr(char - Index)), end="")
    Index = 32 if Index == 0 else 0
