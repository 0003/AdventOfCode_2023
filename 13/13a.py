"""--- Day 13: Point of Incidence ---"""
 #works

def get_reflected(string_pattern,left_index):
    reflected = []
    og_left_index = left_index
    left_index =  left_index #shown for logic
    right_index = left_index + 1

    flag = True
    # left_index it being zero is okay.
    while 0 <= left_index < len(string_pattern) and 0 < right_index < len(string_pattern):
        if string_pattern[left_index] != string_pattern[right_index]:
            return []
        reflected.append((left_index, right_index))
        left_index  -= 1
        right_index += 1
    
    return reflected

def check_for_reflection(pattern):
    #pattern is the block, string_pattern is the line

    #this is a true false list i's are c_indices and j's are the whethe that i was reflective in a pattern
    left_index_reflections = [[False for _ in pattern] for i_ in pattern[0]]

    for i, string_pattern in enumerate(pattern):
        for left_index, c_ in enumerate(string_pattern):
            if get_reflected(string_pattern, left_index):
                left_index_reflections[left_index][i] = True
            else:
                left_index_reflections[left_index][i] = False
    
    #assumes there is only 1 reflection that is true across an entire pattern search
    reflected_indexes = [left_index for left_index, b in enumerate(left_index_reflections) if all(b)] # should just be one
    
    if reflected_indexes:
        print(reflected_indexes)
        reflected_index = reflected_indexes[0]
    else:
        return "NO REFLECTION FOUND"
    
    print("".join([str(i) for i,_ in enumerate(pattern[0])]))
    for i_, string_pattern in enumerate(pattern):
        for left_index, c in enumerate(string_pattern):
            if left_index == reflected_index:
                print(f"\033[91m{c}\033[0m",end="")
            else:
                print(f"{c}",end="")
        print("\t")

    return reflected_index


def find_reflection_index_vertical_or_horizontal(pattern):
    #case there is a vertical pattern
    reflected_ix_vertical = check_for_reflection(pattern)
    if reflected_ix_vertical != "NO REFLECTION FOUND":
        return (reflected_ix_vertical,True)
    else:
    #case there is a horizontal pattern
    #transpose and to leverage function
        pattern_transposed = list(zip(*pattern))
        reflected_ix_horizontal = check_for_reflection(pattern_transposed)

        if reflected_ix_horizontal != "NO REFLECTION FOUND":
            return (reflected_ix_horizontal,False)
        else:
            return ("NO REFLECTION FOUND",False) #this happens if there is no pattern
            #raise Exception(f"This should not have happened {pattern}")
    

def get_input(f):
    with open(f"13/{f}") as fi:
        patterns = []
        pattern = []
        for string_ in fi:
            string_ = string_.strip()
            if string_ == "":
                patterns.append(tuple(pattern))
                pattern = []
            else:
                pattern.append(string_)

    patterns.append(pattern) #get the last one
    return patterns

def main(f):
    patterns = get_input(f)
    
    total = 0
    for i, pattern in enumerate(patterns):
        res_ix, res_vertical_bool = find_reflection_index_vertical_or_horizontal(pattern)
        if res_ix == "NO REFLECTION FOUND":
            print(f'{i} {res_ix=} adjusted_ix=NA {total=} {res_vertical_bool=}')
            break
        adjusted_ix = res_ix + 1 # to correct for indexing being 1 in problem definition
        if res_vertical_bool == True:
            total += adjusted_ix
        elif res_vertical_bool == False:
            total += adjusted_ix  * 100
        print(f'{i} {res_ix=} {adjusted_ix} {total=} {res_vertical_bool=}')
    
    print(total)
    return total

#function tests:
"""s = "#.##..##."
for i,_ in enumerate(s):
    print(f"{i=} {get_reflected(s,i)=}")"""

#print(check_for_reflection(get_input('test.txt')[0]))
#print(check_for_reflection(get_input('test.txt')[1]))

#main('test.txt') # 405 works
#main('test2.txt') # 709 works
#main('test3.txt') #11 works
#main('test4.txt') #this is the one to work on. its an edge case
#main('test4a.txt') #this is the one to work on. its an edge case
main('input.txt')


