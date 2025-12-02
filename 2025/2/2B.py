def get_ids(line):
    id_ranges = range(int(line[0]), int(line[1]) + 1)
    return id_ranges

def invalid(s):
    mid_ix = len(s) // 2
    candidate_strings = [s[:i] for i in range(1, mid_ix + 1) if s[:i]]
    for cs in candidate_strings:
        len_cs = len(cs) #if len 3, then 012 345 678
        groups = [s[j*len_cs:(j+1)*len_cs] for j in range((len(s) + len_cs - 1) // len_cs)] #final debug
        test = all(x == cs for x in groups)
        #print(f" {s = } {cs = } {groups = } {test = }")
        if test:
            #print("above passed")
            #print(f" {s = } {cs = } {groups = } {test = }")
            return len(groups)
    return 0



def main(f):
    res = 0    
    with open(f"{f}") as fi:
        lines = fi.readlines()[0].split(",")
        for ix, line in enumerate(lines):
            id_ranges = get_ids(line.split("-")) #range obj
            for id in id_ranges:
                string_id = str(id)
                if invalid(string_id) >= 2:
                    res += id #id is an int so ok
                #print(f"{ix = } {id = } {res = }")
        print(f"{ix = } {res = }")
    return res

#main("2025/2/simpletest.txt")
#main("2025/2/test.txt")
main("2025/2/input.txt")