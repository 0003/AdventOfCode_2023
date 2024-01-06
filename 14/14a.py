import numpy as np

STONE = "O"
ROCK = "#"
SPACE  = "."

BLOCKED_OBJECTS = (ROCK)

NORTH = (-1,0)
SOUTH = (1,0)
EAST = (0,1)
WEST = (0,-1)

TILT = [NORTH,SOUTH,EAST,WEST]

def can_stone_move(platform,i,j,t):
    assert platform[i][j] == STONE
    
    #if north
    if t == NORTH:
        if i == 0 or platform[i-1][j] == ROCK:
            return False
        if platform[i-1][j] == STONE:
            return True if can_stone_move(platform,i-1,j,NORTH) else return False
        if platform[i-1][j] == SPACE:
            return True           
            
            
    #if south

    #if east

    #if west
    
    #check if 
    return True if condition else False

def get_input(f):
    with open(f"14/{f}") as fi:
        return  [i.strip() for i in fi.readlines()]


def main(f):
    platform = get_input(f)
    print(platform)

main("test.txt")

