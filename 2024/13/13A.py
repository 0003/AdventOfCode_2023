
#works
from itertools import cycle
import re
from math import lcm , gcd

PATTERN = r'\d+\d+'
CYCLE_ACTIONS = ["A","B","P","X"]

class DFS:
    def __init__(self, game : tuple[tuple[int,int],tuple[int,int],tuple[int,int]]):
        self.a, self.b, self.p = game
        self.ax, self.ay = self.a[0], self.a[1] #3 coins
        self.bx, self.by = self.b[0], self.b[1] #1 coins
        self.px, self.py = self.p[0], self.p[1]
        
    def run(self):
            
        visited = set()
        stack = [(0,0,0,0,0)] # distance_x, distance_y, cost,Aqty,Bqty
        cost_qtys = [] #cost, #Aqty, #Bqty

        while stack:
            distance_x, distance_y, cost,Aqty,Bqty = stack.pop()
            if distance_x == self.px and distance_y == self.py:
                cost_qtys.append((cost,Aqty,Bqty))
                continue
            elif distance_x > self.px and distance_y > self.py:
                continue
            else:
                at = (distance_x + self.ax, distance_y + self.ay , cost + 3, Aqty + 1, Bqty )
                bt = (distance_x + self.bx, distance_y + self.by , cost + 1, Aqty, Bqty + 1 )
                for t in (at,bt):
                    if t not in visited:
                        visited.add(t)
                        stack.append(t)
        cost_qtys = sorted(cost_qtys,key= lambda x: x[0])
        #print(f"{cost_qtys = }")

        if len(cost_qtys) > 0:
            return cost_qtys[0][0]
        else:
            return 0

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
    costs = 0 
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
            gdfs = DFS(game)
            cost = gdfs.run()
            print(f"{i = } {cost = }")
            costs += cost
    print(f"Answer: {costs = }")
    return costs
        
        
        

        

#main('test.txt')
main('input.txt')