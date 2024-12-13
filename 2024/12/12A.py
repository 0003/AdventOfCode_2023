#wip
from termcolor import cprint
from collections import defaultdict


PADDING = "#"

def get_perimeter(garden,i,j):
    symbol = garden[i][j]
    symbol_neighbors = 0
    if garden[i-1][j] == symbol:
        symbol_neighbors += 1
    if garden[i+1][j] == symbol:
        symbol_neighbors += 1
    if garden[i][j-1] == symbol:
        symbol_neighbors += 1
    if garden[i][j+1] == symbol:
        symbol_neighbors += 1
    perimeter = 4 - symbol_neighbors

    return perimeter

def get_area(id : int, lookup : dict):

    return len(lookup[id])


def print_garden(garden):
    for i, row in enumerate(garden):
        for j, c in enumerate(row):
            cprint(c, 'light_green', attrs=["dark"], end="")
        print(end='\n')

    return


def get_input(f):
    with open(f"2024/12/{f}") as fi:
        garden = [PADDING + line.strip() + PADDING for line in fi.readlines()]
        garden = [PADDING * len(garden[0])] + garden + [PADDING * len(garden[0])] 
        cprint(garden, 'light_green', attrs=["dark"])
        print_garden(garden)

        return garden

def main(f):

    garden = get_input(f)
    """ 
    for each ij assign symbol to a dict that has ij: done
    for each symbol key in the dictionary:
        
        for each ij traverse
            for each traverse get:
                area
                perimeter
        
    """
    symbols_dict = defaultdict(list)

    for i , row in enumerate(garden):
        for j, c in enumerate(row):
            if c != PADDING:
                symbols_dict[c].append((i,j))
    
    id_plots_dict = defaultdict(list[tuple])
    id = 0
    visited_ijs = set() #ij
    for symbol_char in symbols_dict.keys():
        ijs = symbols_dict[symbol_char]
        same_symbols = set()
        for ij in ijs:
            ij
                


                                    
            #traverse and get visited
            #for each visited throw into a id_plots_dict KEY : ID Values: List of 2 element Tuple



    return
main('test1.txt')