
#wip
from itertools import cycle
import re

PATTERN = r'\d+\d+'
CYCLE_ACTIONS = ["A","B","P","X"]

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