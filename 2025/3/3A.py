import collections

def main(f):
     # key = number, values: tuple of cols, rows
    number_locations = collections.defaultdict(list)
    with open(f"{f}") as fi:
        lines = [line.strip() for line in fi.readlines()]
        lines = [[int(n) for n in line] for line in lines]
        max_col = len(lines[0])
        max_rows = len(lines)
        #building locations in case this is needed
        for row_ix, row in enumerate(lines):
            for col_ix, number in enumerate(row):
                number_locations[number].append( (row_ix,col_ix) )
        res = 0

        for row_ix, row in enumerate(lines):
            row_num_locations = collections.defaultdict(list)
            for col_ix, number in enumerate(row):
                row_num_locations[int(number)].append(col_ix)
            toggle = True

            #find max value before last digit since battery has to be 2 digits
            max_n = max(row[:-1])
            starting_ix = row[:-1].index(max_n)
            
            outer_break = False
            for candidate_n in range(9,-1,-1): #int
                candidate_ixs = row_num_locations[candidate_n] #list of ints of indexes
                for candidate_ix in candidate_ixs:
                    if candidate_ix > starting_ix:
                        row_res = max_n*10 + candidate_n
                        res += max_n*10 + candidate_n #this only works if 2 digit number
                        outer_break = True
                        print(f"{row_ix = } {max_n = } {candidate_n = } {row_res = } {res = }")
                        break
                if outer_break == True:
                    break
        print(f"Done: {row_ix = } {max_n = } {candidate_n = } {row_res = } {res = }")

        return res







#main("2025/3/test.txt")
main("2025/3/input.txt")
