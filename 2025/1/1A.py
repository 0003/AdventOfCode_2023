#hohoho

def value_after_rotate(start,spins):
        return (start + spins) % 100

def main(f):    
    with open(f"{f}") as fi:
        start = 50
        counts = 0
        lines = fi.readlines()
        for line in lines:
            s = line.strip()
            spins = int(s[1:])
            if s[0] == "L":
                start = value_after_rotate(start,-spins)
            else:
                start = value_after_rotate(start,spins)
            if start == 0:
                 counts +=1
            print(f"{s =} and {start = }")
    print(f"{counts = }")
    
#main("2025/1/test.txt")
main("2025/1/input.txt")