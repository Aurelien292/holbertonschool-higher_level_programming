#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = " ".join(str.split()[5:7] + ["with", str.split()[0]])
print(str)
