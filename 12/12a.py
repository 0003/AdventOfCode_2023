"""--- Day 12: Hot Springs ---
"""
#works

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

#length of numbers is the number of groups

#approach 1 learn regular expressions more in terms of how to do meta-patterns
#approach 2 code this out

import itertools

def validate_record(array,record_counts):
    record = "".join(array)
    string_ix = 0
    if sum(record_counts) != sum((1 if c == "#" else 0 for c in record)):
        return False
    for i, rc in enumerate(record_counts):
        group_ix = 0
        first_damaged = False
        while rc > 0 and string_ix <= len(record):
            damaged_remaining = sum((n for n in record_counts[i + 1 :])) + rc
            damageds_in_rest_of_record =  sum([1 if c == "#" else 0 for c in record[string_ix:]])
            if damaged_remaining > damageds_in_rest_of_record:
                #print(f"{record=} is is NOT valid and should NOT fit {record_counts=}")
                return False
            if string_ix > 0 and group_ix == 0:
                if record[string_ix] != ".":
                    return False 
            #print(f"{i=} {damaged_remaining=} {damageds_in_rest_of_record=} {string_ix=}") 

            if record[string_ix] == "#":
                rc -= 1
                string_ix +=1
                group_ix +=1
                first_damaged = True
                if string_ix + 1 < len(record):
                                        #note this is new string_ix
                    if rc == 0 and record[string_ix] != ".":
                       # print(f"{record=} is is NOT valid and should NOT fit {record_counts=}")
                        return False
            elif record[string_ix] == ".":
                if first_damaged == True:
                    #print(f"{record=} is is NOT valid and should NOT fit {record_counts=}")
                    return False #end of contiguous but rc doesn't equal 0
                string_ix +=1
                group_ix +=1       
    if rc > 0:
        return False
    #print(f"{record=} is is valid and should fit {record_counts=}")
    return True

            
def gen_combos(array):
    unknown_indexes =  [i for i , c in enumerate(array) if c == "?"]
    combo_unknowns = itertools.product(*[[".","#"] for _ in unknown_indexes])
    for combo in combo_unknowns:
        new_array = []
        combo_ix = 0
        for i, c in enumerate(array):
            if i in unknown_indexes:
                new_array.append(combo[combo_ix])
                combo_ix +=1
            else:
                new_array.append(c)
        yield new_array


def get_input(f):
    with open(f) as fi:
        rows = []
        for ix in fi:
            _ = ix.split(" ")
            s = _[0]
            tuple_of_counts = [int(x) for x in  _[1].strip().split(",")]
            rows.append((s, tuple_of_counts))
    return rows

def main(f):
    rows = get_input(f'12/{f}')
    total_valid_combos = 0
    for i , r in enumerate(rows):
        print(f"{i}: {r[0]} {r[1]}")
        record_array = [c for c in r[0]]
        record_counts = r[1]
        valid_combos = 0
        for ii, potential_record in enumerate(gen_combos(record_array)):
            #print(f"row: {i} {record_array=} {ii} {potential_record=}")
            if validate_record(potential_record,record_counts):
                #print(f"{potential_record=} is valid {record_counts=}")
                valid_combos += 1
                continue
        total_valid_combos += valid_combos
        print(f"{valid_combos=}")
    print(total_valid_combos)

    return total_valid_combos


#main("test.txt")
#main("test2.txt")

main("input.txt")