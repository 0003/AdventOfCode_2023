"""--- Day 14: Parabolic Reflector Dish ---"""
#works

import numpy as np
import itertools as it
import hashlib
import sys
import math

PART_II_CYCLE = 1000000000

STONE = "O"
ROCK = "#"
SPACE  = "."

NORTH = (-1,0)
SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)

RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def hash_plafrom_cycle(plaftform):
    concatentation = "".join(["".join(e) for e in plaftform])
    #print(f"{concatentation=}")
    #hash_platform = hashlib.sha256(concatentation.encode()).hexdigest()
    #print(hash_platform)
    return concatentation

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
        if i - 1 < 0:
            return False
        if i == 0 or platform[i-1][j] == ROCK:
            result = False
        elif platform[i-1][j] == STONE:
            result = True if can_stone_move(platform,i-1,j,NORTH) else False
        elif platform[i-1][j] == SPACE:
            result = True           
              
    #if south
    if t == SOUTH:
        if i + 1 >= len(platform):
            return False
        if i == len(platform) or platform[i+1][j] == ROCK:
            result = False
        elif platform[i+1][j] == STONE:
            result = True if can_stone_move(platform,i+1,j,SOUTH) else False
        elif platform[i+1][j] == SPACE:
            result = True       

    #if east
    if t == EAST:
        if j + 1 >= len(platform):
            return False
        if j == len(platform[i]) or platform[i][j+1] == ROCK:
            result = False
        elif platform[i][j+1] == STONE:
            result = True if can_stone_move(platform,i,j+1,EAST) else False
        elif platform[i][j+1] == SPACE:
            result = True 

    #if west
    if t == WEST:
        if j - 1 < 0:
            return False
        if j == 0 or platform[i][j-1] == ROCK:
            result = False
        elif platform[i][j-1] == STONE:
            result = True if can_stone_move(platform,i,j-1,WEST) else False
        elif platform[i][j-1] == SPACE:
            result = True 

    return result

def calc_load(platform):
    total = 0
    weights = range(len(platform),0,-1)
    for i,s in enumerate(platform):
        weight_index = weights[i]
        counts_stones = sum((1 if c == STONE else 0 for c in s))
        score = weight_index * counts_stones
        total += score        
        #print(f"{i} {s} {weight_index=} {counts_stones=} {score=} {total=}")
    
    return total

def get_input(f):
    with open(f"14/{f}") as fi:
        return  [list(i.strip()) for i in fi.readlines()]


def main(f):
    platform = get_input(f)

    cycle = 0
    print(f"{cycle=}")
    matrix_print(platform)

    hashes_ix = dict()
    cycle_weights = dict()
    
    #starting from the "top" is most efficient
    for tilt in it.cycle([NORTH,WEST,SOUTH,EAST]):
        flag = True

        #need to do something with to the platform to take advantage of the top bottom effect
        #made a drawing on https://excalidraw.com/ that shows this
        if tilt == NORTH:
            while flag: 
                flag = False
                for i,s in enumerate(platform):
                    for j,c in enumerate(s):
                        if can_stone_move(platform,i,j,tilt): #TODO THIS WILL NEED TO BE UPDATED FOR THE TILT
                                platform[i-1][j] = STONE
                                platform[i][j] = SPACE
                                flag = True
        elif tilt == WEST:
            while flag:
                flag = False
                for i,s in enumerate(platform):
                    #start left and go right
                    for j,c in enumerate(s):
                        if can_stone_move(platform,i,j,tilt): #TODO THIS WILL NEED TO BE UPDATED FOR THE TILT
                                platform[i][j-1] = STONE
                                platform[i][j] = SPACE
                                flag = True        

        elif tilt == SOUTH:
            while flag:
                flag = False
                #start from bottom and work up
                for i in range(len(platform)-1,-1,-1):
                    for j,c in enumerate(platform[i]):
                        if can_stone_move(platform,i,j,tilt): #TODO THIS WILL NEED TO BE UPDATED FOR THE TILT
                                platform[i+1][j] = STONE
                                platform[i][j] = SPACE
                                flag = True

        elif tilt == EAST:
            while flag:
                flag = False
                for i, s in enumerate(platform):
                    #since we are starting from the right and working our way "back"
                    for j  in range(len(s)-1,-1,-1):
                            #adding to the right
                            if can_stone_move(platform,i,j,tilt): #TODO THIS WILL NEED TO BE UPDATED FOR THE TILT
                                platform[i][j+1] = STONE
                                platform[i][j] = SPACE
                                flag = True
            cycle += 1
            weight = calc_load(platform)
            cycle_weights[cycle] = weight

            h = hash_plafrom_cycle(platform)
            print(f"{cycle=} {weight=} {sys.getsizeof(hashes_ix)=} {len(hashes_ix)=}")
            #matrix_print(platform)
            if h in hashes_ix.keys():
                first  = hashes_ix[h]
                second = cycle
                cycle_length = second - first
                print(f" This cycle has already appeared: {first=} {second=} {cycle_length=}")
                return_cycle = ((PART_II_CYCLE - first) % cycle_length) + first
                print(f"{return_cycle=} {cycle_weights[return_cycle]=}" )
                break
            else:
                hashes_ix[h] = cycle
    return cycle_weights[return_cycle]

    


#main("test.txt")
main("input.txt")

