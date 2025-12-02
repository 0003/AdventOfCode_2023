def get_ids(line):
    id_ranges = range(int(line[0]), int(line[1]) + 1)
    return id_ranges

def invalid(s):
    len_s = len(s)
    if len_s % 2 == 0:
        mid_ix = len_s // 2
        if s[:mid_ix] == s[mid_ix:]:
            return True
    return False

def main(f):
    res = 0    
    with open(f"{f}") as fi:
        lines = fi.readlines()[0].split(",")
        for ix, line in enumerate(lines):
            id_ranges = get_ids(line.split("-")) #range obj
            for id in id_ranges:
                string_id = str(id)
                if invalid(string_id):
                    print(f"found {string_id =}")
                    res += id #id is an int so ok
                #print(f"{ix = } {id = } {res = }")
    print(f"{res = }")
    return res


#main("2025/2/test.txt")
main("2025/2/input.txt")