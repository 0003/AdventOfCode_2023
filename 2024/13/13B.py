
#works
from itertools import cycle
import re
from math import lcm , gcd
import numpy as np

PATTERN = r'\d+\d+'
CYCLE_ACTIONS = ["A","B","P","X"]

class Game:
    def __init__(self, game : tuple[tuple[int,int],tuple[int,int],tuple[int,int]],part2=False):
        adder = 0 if part2 == False else 10000000000000
        self.a, self.b, self.p = game
        self.ax, self.ay = self.a[0], self.a[1] #3 coins
        self.bx, self.by = self.b[0], self.b[1] #1 coins
        self.px, self.py = self.p[0] + adder, self.p[1] + adder
        
    def run(self):
        Aqty = (self.bx*self.py - self.by*self.px) / (self.bx*self.ay - self.by*self.ax)
        Bqty = (self.px-self.ax*Aqty) / self.bx

        if abs(Aqty - round(Aqty)) < 0.0000001 and abs(Bqty - round(Bqty)) < 0.0000001:
            return 3*Aqty + Bqty
        else:
            return 0

def int_check(n,epsilon = 0.0001):
    if abs(round(n) - n) < epsilon:
        return True
    else:
        return False

def get_game_value(s):
    m = re.findall(PATTERN,s)
    ret =  tuple(int(ss) for ss in m)
    return ret

def get_input(f):
    with open(f"2024/13/{f}") as fi:
        lines = [x.strip() for x in fi]
        return lines

def main(f,part2):
    lines = get_input(f)
    games = [] # tuples of A (x,y) B (x,y) P (x,y)
    cycle_action_ = cycle(CYCLE_ACTIONS)
    costs = 0 
    lines.append(" ")
    for i, line in enumerate(lines):
        cycle_action = next(cycle_action_)

        if cycle_action == "A":
            a = get_game_value(line)
        elif cycle_action == "B":
            b = get_game_value(line)
        elif cycle_action == "P":
            p = get_game_value(line)
        elif cycle_action == "X":
            game = (a,b,p)
            games.append(game)
            gdfs = Game(game,part2)
            cost = gdfs.run()
            print(f"{i = } {cost = }")
            costs += cost
    print(f"Answer: {int(costs) = }")
    return int(costs)
        
        
#main('test.txt',True)
#main('test.txt',False)

main('input.txt',True)
#main('input.txt',False)
