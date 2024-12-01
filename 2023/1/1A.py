"""--- Day 1: Trebuchet?! ---"""

#works__

import numpy as np
import re

def get_input() -> np.ndarray:
    with open('input.txt','r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    array = np.array(lines)
    return array

def line_to_digits(s: str) -> int:
    digits = re.findall(r'\d',s)
    if len(digits) == 1:
        return int(digits[0]*2)
    else:
        return int(digits[0]+digits[-1])

def main():
    a = get_input()
    list_of_right_digits = [line_to_digits(s) for s in a ]
    result = sum(list_of_right_digits)
    print (result)
    return result

main()