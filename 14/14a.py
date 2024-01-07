"""--- Day 14: Parabolic Reflector Dish ---"""
#works

import numpy as np
import copy
import functools

STONE = "O"
ROCK = "#"
SPACE  = "."

NORTH = (-1,0)
SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)

TILT = [NORTH,SOUTH,EAST,WEST]

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def matrix_print(platform):
    for i,s in enumerate(platform):
        print(f"{i=}  ",end="")
        for j, c in enumerate(s):
            color = RED if c == STONE else GREEN if c == ROCK else CYAN
            print(f"{color + c + RESET}", end="")
        print("\t")
    print("\t")

def can_stone_move(platform,i,j,t):
    if platform[i][j] in (ROCK,SPACE):
        return False
 
    #if north
    if t == NORTH:
        if i == 0 or platform[i-1][j] == ROCK:
            result = False
        elif platform[i-1][j] == STONE:
            result = True if can_stone_move(platform,i-1,j,NORTH) else False
        elif platform[i-1][j] == SPACE:
            result = True           
            
            
    #if south

    #if east

    #if west
    
    #check if 
    return result

def calc_load(platform):
    total = 0
    weights = range(len(platform),0,-1)
    for i,s in enumerate(platform):
        weight_index = weights[i]
        counts_stones = sum((1 if c == STONE else 0 for c in s))
        score = weight_index * counts_stones
        total += score        
        print(f"{i} {s} {weight_index=} {counts_stones=} {score=} {total=}")
    
    return total

def get_input(f):
    with open(f"14/{f}") as fi:
        return  [list(i.strip()) for i in fi.readlines()]


def main(f):
    platform = get_input(f)
    matrix_print(platform)
    og_platform = copy.deepcopy(platform)

    #starting from the "top" is most efficient
    flag = True
    while flag:
        flag = False
        for i,s in enumerate(platform):
            for j,c in enumerate(s):
                if can_stone_move(platform,i,j,NORTH):
                    platform[i-1][j] = STONE
                    platform[i][j] = SPACE
                    flag = True

    matrix_print(platform)
    weight = calc_load(platform)

    


#main("test.txt")
main("input.txt")

