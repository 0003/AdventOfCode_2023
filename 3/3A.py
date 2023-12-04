"""--- Day 3: Gear Ratios ---
You and the Elf eventually reach a gondola lift station; he says the gondola lift will take you up to the water source, but this is as far as he can bring you. You go inside.

It doesn't take long to find the gondolas, but there seems to be a problem: they're not moving.

"Aaah!"

You turn around to see a slightly-greasy Elf with a wrench and a look of surprise. "Sorry, I wasn't expecting anyone! The gondola lift isn't working right now; it'll still be a while before I can fix it." You offer to help.

The engineer explains that an engine part seems to be missing from the engine, but nobody can figure out which one. If you can add up all the part numbers in the engine schematic, it should be easy to work out which part is missing.

The engine schematic (your puzzle input) consists of a visual representation of the engine. There are lots of numbers and symbols you don't really understand, but apparently any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. (Periods (.) do not count as a symbol.)

Here is an example engine schematic:

467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
In this schematic, two numbers are not part numbers because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol and so is a part number; their sum is 4361.

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?"""

#works_

import numpy as np
import re
from functools import reduce
from operator import mul

#get space
#for each a in A, determine number group, get each index number in the number group, determine if they are next to a symbol.



def get_dimensions_of_input(a):
    rows = len(a)
    cols = len(a[0])
    return rows, cols

def is_symbol(s):
    try:
        if not (s.isdigit() or s == '.'):
            print(s, "is a symbol")
            return True
        else:
            print(s, "is not a symbol")
            return False 
    except IndexError:
        print("Index Error not in range")
        return False 
    
def near_symbol(a,i,j,part_number,tests_ran):
    print("test #:",tests_ran," near symbol i:", i, " j:", j, "which is: ",a[i][j], "in: ", part_number)
    try:
        top_left = is_symbol(a[i-1][j-1])
    except IndexError:
        top_left = False
    try:
        top = is_symbol(a[i-1][j])
    except IndexError:
        top = False
    try:
        top_right = is_symbol(a[i-1][j+1])
    except IndexError:
        top_right = False
    try:
        right = is_symbol(a[i][j+1])
    except IndexError: 
        right = False
    try:
        bottom_right = is_symbol(a[i+1][j+1])
    except IndexError:
        bottom_right = False
    try:
        bottom = is_symbol(a[i+1][j])
    except IndexError:
        bottom = False
    try:
        bottom_left = is_symbol(a[i+1][j-1])
    except IndexError:
        bottom_left = False
    try:
        left = is_symbol(a[i][j-1])
    except IndexError:
        left = False

    if top_left or top or top_right or right or bottom_right or bottom or bottom_left or left:
        return True 
    else:
        return False

def input() -> np.ndarray:
    with open('3/input.txt','r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return lines

def main():
    a = input()
    """cols = get_dimensions_of_input(a)[1]
    new_a = ["."*cols]
    for row_s in a:
        row_s = "."+row_s+"."
        new_a.append(row_s)
    new_a.append("."*cols)
    a = np.array(new_a)"""
    a = np.array(a)

    rows, cols = get_dimensions_of_input(a)
    print(f"new a:\n",a)
    
    print ("rows: ", rows)
    print ("cols: ", cols)

    valid_part_numbers = []
    i = -1
    for row in a:
        i += 1
        candidates = [(match.group(), match.start(), match.end()) for match in re.finditer(r'\d+',row)]
        print("printing candidates: ", candidates)
        for candidate in candidates:
            part_number = int(candidate[0])
            start = candidate[1]
            end = candidate[2]
            tests_ran = 0
            for j in range(start,end):
                tests_ran += 1
                if near_symbol(a,i,j,part_number,tests_ran):
                    valid_part_numbers.append(part_number)
                    print("~END: part number: ",part_number, "is valid")
                    break
                else:
                    pass
            print("~END: part number: ", part_number, "is not valid")
    print(valid_part_numbers)
    print(sum(valid_part_numbers))                
    result = sum(set(valid_part_numbers))
    print(result)

    return result

main()