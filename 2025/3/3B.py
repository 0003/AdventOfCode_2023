import collections

def main(f):
     # key = number, values: tuple of cols, rows
    number_locations = collections.defaultdict(list)
    with open(f"{f}") as fi:
        lines = [line.strip() for line in fi.readlines()]
        lines = [[int(n) for n in line] for line in lines]

        res = 0


        for row_ix, row in enumerate(lines):
            digits_left = 12
            jolts = []
            row_num_locations = collections.defaultdict(list)
            for col_ix, number in enumerate(row):
                row_num_locations[int(number)].append(col_ix)

            starting_ix = -1
            while digits_left > 0:
                best_ix_candidate = None
                best_ix_candidate_n = None

                for candidate_n in range(9,-1,-1): #int
                    candidate_ixs = row_num_locations[candidate_n] #list of ints of indexes
                    for candidate_ix in candidate_ixs: #this should already be sorted for greedy approach
                        if candidate_ix > starting_ix and len(row) - candidate_ix >= digits_left:
                            best_ix_candidate = candidate_ix
                            best_ix_candidate_n = candidate_n
                            break
                    if best_ix_candidate is not None:
                        break #found one

                if best_ix_candidate is not None:
                    jolts.append(best_ix_candidate_n) 
                    starting_ix = best_ix_candidate
                    digits_left -= 1
                    #print(f"{row_ix = } {jolts =} {max_n = } {candidate_n = }")
                

            jolts_str =  ''.join([str(i) for i in jolts])
            jolts_int = int(jolts_str)
            res += jolts_int
            digits_left = 12
            print(f"Done: {row_ix = } {jolts_int = } {len(str(jolts_int)) =} {res = }")
        print(f"Done: {row_ix = } {jolts_int = } {len(str(jolts_int)) =} {res = }")

        return res







#main("2025/3/test.txt")
main("2025/3/input.txt")
