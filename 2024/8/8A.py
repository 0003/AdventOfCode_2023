#WIP

from collections import defaultdict

class node:
    def __init__(self, symbol : str, loc : tuple):
        self.symbol = symbol
        self.loc = loc
    
def get_ij_distances(a : tuple, b : tuple):
    i = abs(a[0] - b[0])
    j = abs(a[1] - b[1])
    return (i, j)

def get_input(f):
    with open(f"2024/8/{f}") as fi:
        grid = [e.strip() for e in fi]
        return grid

def main(f):
    grid = get_input(f)
    node_locs_by_symbol = defaultdict(list)
    nodes = []

    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char != ".":
                loc = (i,j)
                nodes.append(node(char,loc))
                node_locs_by_symbol[char].append(loc)

#for each symboltype
#for each node of type
#get mirrors ij
#determine if on grid
#add to symbol ij if match (2 spossibilities for i,j add...
#the other symbol and the other is the antinode)
#get clarity on antidote counting
    
    return


        

main("test.txt")