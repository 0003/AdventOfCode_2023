"""--- Day 13: Point of Incidence ---"""
 #works
import copy

def smudge(pattern,i,j):
    pattern2 = list(copy.deepcopy(pattern))
    
    pattern_string = pattern2[i]
    old_char = pattern_string[j]

    if old_char == ".":
        new_char = "#"
    elif old_char == "#":
        new_char = "."
    else:
        raise Exception("This should not happen")
    
    pattern_string_smudge = pattern_string[:j] + new_char + pattern_string[j + 1:]
    pattern2[i] = pattern_string_smudge

    return pattern2


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
        print(f"{reflected_indexes=}")
        return reflected_indexes
    else:
        return [None] 

def find_reflection_index_vertical_or_horizontal_part2(pattern):
    #case there is a vertical pattern
    reflect_set = set()
    reflected_ix_vertical_indices = check_for_reflection(pattern)
    for ix in reflected_ix_vertical_indices:
        if ix != None:
            reflect_set.add(tuple([ix,True]))

    pattern_transposed = list(zip(*pattern))
    reflected_ix_horizontal_indices = check_for_reflection(pattern_transposed)
    for ix in reflected_ix_horizontal_indices:
        if ix != None :
            reflect_set.add(tuple([ix,False]))

    return reflect_set

def find_reflection_index_vertical_or_horizontal_part1(pattern):
    #case there is a vertical pattern
    reflected_ix_vertical = check_for_reflection(pattern)[0]

    if reflected_ix_vertical != None :
        return (reflected_ix_vertical,True)
    else:
    #case there is a horizontal pattern
    #transpose and to leverage function
        pattern_transposed = list(zip(*pattern))
        reflected_ix_horizontal = check_for_reflection(pattern_transposed)[0]

        if reflected_ix_horizontal != None :
            return (reflected_ix_horizontal,False)
        else:
            return (None ,False) #this happens if there is no pattern
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
        res_ix, res_vertical_bool = find_reflection_index_vertical_or_horizontal_part1(pattern)
        og_reflection = set()
        og_reflection.add(tuple([res_ix,res_vertical_bool]))
        print(f'After first run: {og_reflection=}')
        flag = False
        for ii, patern_string in enumerate(pattern):
            if flag == True:
                break
            for jj, _ in enumerate(patern_string):
                if flag == True:
                    break
                pattern2 = smudge(pattern,ii,jj)
                reflections_set = find_reflection_index_vertical_or_horizontal_part2(pattern2)
                print(f"{ii=} {jj=} {reflections_set=}")
                
                """ #commenting this out because Part 2 this will happen a lot
                if res_ix == NOT_FOUND :
                    print(f'{i} {ii=} {jj=} {res_ix=} adjusted_ix=NA {total=} {res_vertical_bool=}')rw
                """
                for res_ix,res_vertical_bool in reflections_set:

                    if isinstance(res_ix,int) and tuple([res_ix,res_vertical_bool]) not in og_reflection:
                        adjusted_ix = res_ix + 1 # to correct for indexing being 1 in problem definition
                        if res_vertical_bool == True:
                            total += adjusted_ix
                        if res_vertical_bool == False:
                            total += adjusted_ix  * 100
                        print(f'After smudging {i} {ii=} {jj=} {res_ix=} {adjusted_ix=} {total=} {res_vertical_bool=}')
                        flag = True
    
    print(f"{total=}")
    return total

#function tests:
"""s = "#.##..##."
for i,_ in enumerate(s):
    print(f"{i=} {get_reflected(s,i)=}")"""

#print(check_for_reflection(get_input('test.txt')[0]))
#print(check_for_reflection(get_input('test.txt')[1]))

#main('test.txt') # 405 works part b 400 works
#main('test2.txt') # 709 works part b 1400 works
#main('test3.txt') #11 works
#main('test4.txt') #this is the one to work on. its an edge case 15
#main('test4a.txt') #this is the one to work on. its an edge case
#main('test5.txt') #part 2: the new reflections are(1) Vertical symmetry after col 5 (2) Vertical symmetry after col 10
#main('test6.txt')
main('input.txt')



