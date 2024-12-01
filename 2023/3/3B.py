"""--- Day 3: Gear Ratios ---

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

def get_input() -> np.ndarray:
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
    a = get_input()
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