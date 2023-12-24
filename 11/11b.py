"""--- Day 11: Cosmic Expansion ---
"""
#works

import copy
import itertools

HEIGHT_EXPANSION = 1000000
WIDTH_EXPANSION = 1000000

def simple_galactic_distance(g1,g2,height_expansions,width_expansions) -> int:
    i1,j1 = g1
    i2,j2 = g2
    
    inflation_height = sum(HEIGHT_EXPANSION-1 for ix in range(min(i1,i2),max(i1,i2)) if ix in height_expansions)
    inflation_width = sum(WIDTH_EXPANSION-1 for ix in range(min(j1,j2),max(j1,j2)) if ix in width_expansions)
    manhattan_distance = inflation_height + abs(i2 - i1) + inflation_width + abs(j2 - j1)
        
    return manhattan_distance


def main(f):
    a = get_input(f)
    #list of strings
    height_expansions = []
    width_expansions = []
    galaxies = [(i,j) for i, r in enumerate(a) for j, r  in enumerate(r) if a[i][j] == "#"]
    print(galaxies)
    print_map(a)
    og_distange = [[(1,1) for c in r] for r in a]

    expansion_distance = copy.deepcopy(og_distange)

    #this is the UpDown distance
    for i, r in enumerate(a):
        if all(c == "." for c in r):
            height_expansions.append(i)
            #for j, c in enumerate(r):
                #expansion_distance[i][j] = (og_distange[i][j][0] * HEIGHT_EXPANSION, og_distange[i][j][1]) 

    #this is the LeftRight distance
    #swap rows for columns
    transposed_a = [''.join(t) for t in zip(*a)]

    """ 
    print(f"Transposed Map:",end='\n')
    print_map(transposed_a) 
    """
    for i, r in enumerate(transposed_a):
        if all(c == "." for c in r):
            width_expansions.append(i)
            #for j, c in enumerate(r):
                #expansion_distance[i][j] = (og_distange[i][j][0], og_distange[i][j][1] * WIDTH_EXPANSION)

    """ 
    print(f"The manhattan distance adj for inglation for:\
          5 and 9 is {simple_galactic_distance(galaxies[4],galaxies[8],height_expansions,width_expansions)}\
          1 and 7 is {simple_galactic_distance(galaxies[0],galaxies[6],height_expansions,width_expansions)}\
          3 and 6 is {simple_galactic_distance(galaxies[2],galaxies[5],height_expansions,width_expansions)}\
          8 and 9 is {simple_galactic_distance(galaxies[7],galaxies[8],height_expansions,width_expansions)}\
            ")
    """
    """
    combos = itertools.combinations(galaxies,2)
    iterative_sum = 0
    for g1,g2 in combos:
        result = simple_galactic_distance(g1,g2,height_expansions,width_expansions)
        iterative_sum += result
        print(f"{(g1,g2)} = {result} total = {iterative_sum}")
    """

    sum_of_simple_inflation_distances_between_galaxies = sum(simple_galactic_distance(g1,g2,height_expansions,width_expansions) for g1, g2 in itertools.combinations(galaxies,2))
    print(sum_of_simple_inflation_distances_between_galaxies)
    return sum_of_simple_inflation_distances_between_galaxies


def get_input(f):
    with open(f"11/{f}") as f:
        return [r.strip() for r in f.readlines()]
    
def print_map(a):
    for r in a:
        for c in r:
            print(f"{c}", end='')
        print("") #break

#main("test1.txt")
main("input.txt")


