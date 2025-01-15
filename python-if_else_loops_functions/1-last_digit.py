#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_d = abs(number) % 10
if number < 0:
    last_d *= -1
if last_d > 5:
    print("Last digit of {:d} is {:d} and is greater\
 than 5".format(number, last_d))
elif last_d == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_d))
elif last_d < 6 and last_d != 0:
    print("Last digit of {:d} is {:d} and is less\
 than 6 and not 0".format(number, last_d))
