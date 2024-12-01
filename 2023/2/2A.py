"""--- Day 2: Cube Conundrum ---"""

#works_

import numpy as np
import re

bag = {'red' : 12, 'green': 13 ,'blue' :14 }

def valid_cube_pull(cube_color,qty):
    if qty <= bag[cube_color]:
        return True
    else:
        return False

def parse_game(s):
    s = s.split(":")
    #contains game id
    s1 = s[0]
    id = re.findall(r'\d+',s1)[0]

    pulls = s[1].split(';')
    for pull in pulls:
        bunch_of_cubes = pull.split(',')
        for cube in bunch_of_cubes:
            cube_elemements = cube.strip().split(' ')
            qty = int(cube_elemements[0])
            cube_color = cube_elemements[1]
            if valid_cube_pull(cube_color,qty):
                pass
            else:
                return 0
    return int(id)

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