#hohoho
def value_and_counts_after_rotate(start,spins):
        value = (start + spins) % 100
        if spins > 0:
            new_counts = (start + spins) // 100
        elif spins < 0:
            #I think we can be smart here and just treat spins as sign netural and back out the edge case
            new_counts = ( -(start + spins) // 100) - ((-start)//100)
        else:
            new_counts = 0
        print(f"{start = } {spins = } {value = } {new_counts = }")
        return value, new_counts

def main(f):    
    with open(f"{f}") as fi:
        start = 50
        counts = 0
        lines = fi.readlines()
        for line in lines:
            s = line.strip()
            spins = int(s[1:])
            res = [0,0]
            if s[0] == "L":
                res = value_and_counts_after_rotate(start,-spins)
            else:
                res = value_and_counts_after_rotate(start,spins)
            start, new_counts = res
            counts += new_counts
            #print(f"{s =} and {start = } and {counts = }")
    print(f"{counts = }")
    
main("2025/1/test.txt")
main("2025/1/test2.txt")
main("2025/1/input.txt")