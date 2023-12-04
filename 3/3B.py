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

Of course, the actual engine schematic is much larger. What is the sum of all of the part numbers in the engine schematic?
The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---
The engineer finds the missing part and installs it in the engine! As the engine springs to life, you jump in the closest gondola, finally ready to ascend to the water source.

You don't seem to be going very fast, though. Maybe something is still wrong? Fortunately, the gondola has a phone labeled "help", so you pick it up and the engineer answers.

Before you can explain the situation, she suggests that you look out the window. There stands the engineer, holding a phone in one hand and waving with the other. You're going so slowly that you haven't even left the station. You exit the gondola.

The missing part wasn't the only issue - one of the gears in the engine is wrong. A gear is any * symbol that is adjacent to exactly two part numbers. Its gear ratio is the result of multiplying those two numbers together.

This time, you need to find the gear ratio of every gear and add them all up so that the engineer can figure out which gear needs to be replaced.

Consider the same engine schematic again:

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
In this schematic, there are two gears. The first is in the top left; it has part numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. (The * adjacent to 617 is not a gear because it is only adjacent to one part number.) Adding up all of the gear ratios produces 467835.

What is the sum of all of the gear ratios in your engine schematic?

"""

#works_

import numpy as np
import re
from functools import reduce
from operator import mul

digits = [str(x) for x in range(10)]

def get_dimensions_of_input(a):
    rows = len(a)
    cols = len(a[0])
    return rows, cols

def is_number_group(a,i,j):
    number = a[i][j]
    if number == '~':
        return (False,None)
    print("ng test - initial:", number)
    if number not in digits:
        return (False,None)
    left_condition = True
    right_condition = True
    left_most_index = 0
    right_most_index = 0
    while left_condition:
        left_most_index += 1
        new_character = str(a[i][j-left_most_index])
        print("nc: ", new_character)        
        if new_character in digits:
            print(left_most_index)   
        else:
            left_condition = False
            left_most_index -= 1
        number = a[i][j-left_most_index:j+1]
        print("ng test - left:", number)
    while right_condition:
        right_most_index +=1
        new_character = str(a[i][j+right_most_index])
        #print("nc: ", new_character)
        if new_character in digits:
            #print(right_most_index)
            pass      
        else:
            right_condition = False
            right_most_index -= 1
        number = a[i][j-left_most_index:j+1+right_most_index]
        #print("ng test - left:", number)
    print("ng - final:", number)
    return (True,number)
    
def near_two_numbers(a,i,j):
    print(" gear i:", i, " j:", j, "which is: ",a[i][j])
    numbers = []
    try:
        top_left = is_number_group(a,i-1,j-1)
        if top_left[0] & (top_left[1] not in numbers):
            numbers.append(top_left[1])
    except IndexError:
        top_left = (False,None)
    try:
        top = is_number_group(a,i-1,j)
        if top[0] & (top[1] not in numbers):
            numbers.append(top[1])
    except IndexError:
        top = (False,None)
    try:
        top_right = is_number_group(a,i-1,j+1)
        if top_right[0] & (top_right[1] not in numbers):
            numbers.append(top_right[1])
    except IndexError:
        top_right = (False,None)
    try:
        right = is_number_group(a,i,j+1)
        if right[0] & (right[1] not in numbers):
            numbers.append(right[1])
    except IndexError: 
        right = (False,None)
    try:
        bottom_right = is_number_group(a,i+1,j+1)
        if bottom_right[0] & (bottom_right[1] not in numbers):
            numbers.append(bottom_right[1])
    except IndexError:
        bottom_right = (False,None)
    try:
        bottom = is_number_group(a,i+1,j)
        if bottom[0] & (bottom[1] not in numbers):
            numbers.append(bottom[1])
    except IndexError:
        bottom = (False,None)
    try:
        bottom_left = is_number_group(a,i+1,j-1)
        if bottom_left[0] & (bottom_left[1] not in numbers):
            numbers.append(bottom_left[1])
    except IndexError:
        bottom_left = (False,None)
    try:
        left = is_number_group(a,i,j-1)
        if left[0] & (left[1] not in numbers):
            numbers.append(left[1])
    except IndexError:
        left = (False,None)
    print(numbers)
    if len(numbers) == 2:
        result =  (True,(i,j),numbers,reduce(mul, [int(x) if all( e in digits for e in x) and isinstance(x,str) else 1 for x in numbers], 1))
        print("Valid gear: ", result)
        return result
    else:
        return (False, (i,j),numbers,0)

def input() -> np.ndarray:
    with open('3/input.txt','r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        cols = len(lines[0])
        padding_line ='~'*(cols+2)
        new_lines = [padding_line]
        print(new_lines)
        for line in lines:
            new_line = "~" + line + "~"
            new_lines.append(new_line)
        new_lines.append(padding_line)
        print("New lines:", new_lines)
    return new_lines

def main():
    a = input()
    a = np.array(a)
    print(a)
    rows, cols = get_dimensions_of_input(a)
    print(f"new a:\n",a)
    
    print ("rows: ", rows)
    print ("cols: ", cols)

    valid_gear_ratios = []
    i = -1
    for row in a:
        i += 1
        candidates = [(match.group(), match.start()) for match in re.finditer(r'\*',row)]
        print("printing candidates: ", candidates)
        for candidate in candidates:
            j = candidate[1]
            valid_gear = near_two_numbers(a,i,j)
            print("Test result :", valid_gear)
            if valid_gear[0] == True:
                valid_gear_ratios.append(valid_gear[3])
    


    print("Valid Ratios: ", "*"*20,"\n",valid_gear_ratios)
    result = sum(valid_gear_ratios)
    print(result)

    return result

main()