
#wip
from itertools import cycle
import re
from math import lcm , gcd

PATTERN = r'\d+\d+'
CYCLE_ACTIONS = ["A","B","P","X"]

def solve_game(game : tuple[tuple[int,int],tuple[int,int],tuple[int,int]]) -> int:
    a, b, p = game
    ax, ay = a[0], a[1] #3 coins
    bx, by = b[0], b[1] #1 coins
    px, py = p[0], p[1]    

    cost = 0
    cheap_x, token_x = (ax,3) if a[0] // b[0] < 3 else (bx,1)
    cheap_y, token_y = (ay,3) if a[0] // b[0] < 3 else (by,1)
    
    not_solved_x = True
    while not_solved_x:
        px // cheap_x
    

def get_game_value(s):
    m = re.findall(PATTERN,s)
    ret =  tuple(int(ss) for ss in m)
    return ret

def get_input(f):
    with open(f"2024/13/{f}") as fi:
        lines = [x.strip() for x in fi]
        return lines

def main(f):
    lines = get_input(f)
    games = [] # tuples of A (x,y) B (x,y) P (x,y)
    cycle_action_ = cycle(CYCLE_ACTIONS)

    for line in lines:
        cycle_action = next(cycle_action_)

        if cycle_action == "A":
            a = get_game_value(line)
        elif cycle_action == "B":
            b = get_game_value(line)
        elif cycle_action == "P":
            p = get_game_value(line)
        elif cycle_action == "X":
            games.append((a,b,p))

    return
        
        
        

        

#main('test.txt')
main('input.txt')