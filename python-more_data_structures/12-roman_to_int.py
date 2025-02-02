#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str:
        return 0
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
    total = 0
    lenght = len(roman_string)
    for i in range(lenght):
        current_value = roman_values[roman_string[i]]
        if i + 1 < lenght and roman_values[roman_string[i+1]] > current_value:
            total -= current_value
        else:
            total += current_value
    return total
