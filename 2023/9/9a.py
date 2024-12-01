"""--- Day 9: Mirage Maintenance ---"""
#works
import re

def calc_next_in(sequence):
    if not any(sequence):  #check if there are any zeros
        return 0 #test

    sequence_of_diffs = [ ]
    for i in range( len(sequence) - 1): #shorten it. This is index. Dont thing enumeration would work here?
        sequence_of_diffs.append( sequence[ i + 1] - sequence[i] ) # 2nd item minus first. Maybe could use zip here??
    return sequence[-1] + calc_next_in(sequence_of_diffs)

def get_input(fi):
    with open(fi) as f:
        return f.readlines()

def parse(fi):
    data = get_input(fi)
    data_ns = [r.strip() for r in data] # remove the newline special char
    data_is = [r.split() for r in data_ns] # split the string into individual strings
    data_int = [list(map(int,r)) for r in data_is] #map objects need to be yielded

    return data_int

def main(fi):
    print(f'{fi}')
    data = parse(fi)
    # data is a parse data of ints
    #the test case said that all sequences after some K amount of succeeding differentiations
    #differentiate to zero

    sums = 0
    for sequence in data:
        sums += calc_next_in(sequence)
        #print(f"sequence: {sequence} next number for f({len(sequence)}) = {next_val}")
    print(f"sums: {sums}")
    
    return sums

main('9/input.txt')
