"""--- Day 2: Cube Conundrum ---"""

#works_

import numpy as np
import re
from functools import reduce
from operator import mul

def parse_game(s):
    s = s.split(":")
    min_colors = {'red' : 0, 'green' : 0, 'blue' :0}
    pulls = s[1].split(';')
    for pull in pulls:
        bunch_of_cubes = pull.split(',')
        for cube in bunch_of_cubes:
            cube_elemements = cube.strip().split(' ')
            qty = int(cube_elemements[0])
            cube_color = cube_elemements[1]
            if qty>min_colors[cube_color]:
                min_colors[cube_color] = qty
    return reduce(mul, min_colors.values(), 1)

def get_input() -> np.ndarray:
    with open('2/input.txt','r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    return np.array(lines)

def main():
    a = get_input()
    valid_game_ids = [parse_game(s) for s in a]  
    print(valid_game_ids)
    result = sum(valid_game_ids)
    print (result)
    return result

main()