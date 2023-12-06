"""--- Day 1: Trebuchet?! ---"""

#works__

import numpy as np
import re

all_digits_and_spellings = ['0', 'zero', '1', 'one', '2', 'two', '3', 'three', '4', 'four', '5', 'five',
                             '6', 'six', '7', 'seven', '8', 'eight', '9', 'nine']
spelling_to_int =  {all_digits_and_spellings[i + 1]: all_digits_and_spellings[i] for i in range(0, len(all_digits_and_spellings), 2)}
spelling_to_int_keys = spelling_to_int.keys()

print(spelling_to_int)

re_pattern_string = '|'.join(all_digits_and_spellings)
re_pattern = re.compile(rf'(?:{re_pattern_string})')
                      
def get_input() -> np.ndarray:
    with open('input.txt','r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    array = np.array(lines)
    return array

def line_to_digits(s: str) -> int:
    digits = re_pattern.findall(s)
    foo = lambda x: spelling_to_int[x] if x in spelling_to_int_keys else x
    digits = [foo(x) for x in digits]
    if len(digits) == 1:
        return int(digits[0]*2)
    else:
        return int(digits[0]+digits[-1])

def main():
    a = get_input()
    list_of_right_digits = [line_to_digits(s) for s in a ]
    print(list_of_right_digits[:5])
    result = sum(list_of_right_digits)
    print (result)
    return result

main()