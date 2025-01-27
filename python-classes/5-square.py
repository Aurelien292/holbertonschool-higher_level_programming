#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def my_print(self):
        if self.__size != 0:
            print(("#" * self.__size + '\n') * self.__size, end='')
        else:
            print(end='\n')

    def area(self):
        return self.__size ** 2
