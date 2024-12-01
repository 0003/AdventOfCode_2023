"""--- Day 12: Hot Springs ---
"""

"""
operational : .
damadaged  : # 
unknown : ?

numbers are the sum of the damaged parts for each group in order

groups always separated by a operational part
So rule 1 that a . must either start or end with a . depending on the last group

Rule 2 all groups must be valid

Return sum of all different arrangemetns of all results
"""


#works
import functools

@functools.lru_cache
def solver(record_string, record_counts) -> int:
    #base case from string perspective
    if record_string == "":
        if record_counts == ():
            return 1 #finishes
        else:
            return 0 # finished th length of the record, but we still have record_counts
        
    #base case from counts perspective   
    if record_counts == ():
        if "#" not in record_string: # if the counts are all gone, then there cannot be a # left
            return 1 # this is the other side of it, so this also is a finish
        else:
            return 0 #failed
    
    #non-base case
    result = 0

    char = record_string[0]
    if char in "?.":
        #advance string one and keep record_counts as is
        result += solver(record_string[1:],record_counts)
    
    #this is key before it was an elif, but need to consider that ? is either a "." or a "?"
    if char in "?#":
        #check count
        next_count = record_counts[0] 
        if next_count <= len(record_string):
            #then there cannot be a "." in the rest of the string
            if "." not in record_string[:next_count]: # there cannot be a "." because it's cpntiguous
                # both perspectives
                if next_count == len(record_string) or record_string[next_count] != "#":
                    #jumpahead on the ###'s that we know have to exist and move to the next record_counts
                    result += solver(record_string[next_count + 1:], record_counts[1:])
        #Here would be elses that I have removed
    return result


def get_input(f):
    with open(f) as fi:
        rows = []
        for ix in fi:
            _ = ix.split(" ")
            s = "?".join([_[0]] * 5)
            tuple_of_counts = tuple(int(x) for x in  _[1].strip().split(",")) * 5
            rows.append((s, tuple_of_counts))
    return rows

def main(f):
    rows = get_input(f'12/{f}')
    total_valid_combos = 0
    for i , r in enumerate(rows):
        record_string = r[0]
        record_counts = r[1]
        total_valid_combos += solver(record_string,record_counts)
        print(f"{i}: {r[0]} {r[1]} {total_valid_combos=}")

    print(f"{total_valid_combos=}")  
    return total_valid_combos


#main("test.txt")
#main("test2.txt")
#main("test3.txt")

main("input.txt") 