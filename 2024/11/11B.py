#works
from functools import lru_cache

@lru_cache(maxsize=10000)
def blinks(stone, blinks_left):
    chars = str(stone)
    if blinks_left == 0:
        return 1 
    
    elif stone == 0:
        return blinks(1, blinks_left - 1)
    
    elif len(chars) % 2 == 0:
        ix = (len(chars) // 2)
        stone_a = int(chars[:ix])
        stone_b = int(chars[ix:])
        return blinks(stone_a, blinks_left - 1) + blinks(stone_b, blinks_left - 1)
            
    else:
        return blinks(stone*2024, blinks_left - 1)


def get_input(f):
    with open(f'2024/11/{f}') as fi:
        stones = [int(e) for line in fi.readlines() for e in line.split(" ")]
        print(stones)
        return stones

def main(f,times=75):
    stones = get_input(f)
    counts = []
    for stone in stones:
        counts.append(blinks(stone, times))
    print(f"{sum(counts) = }")
    return counts

#main("testalpha.txt",1)
#main('test.txt',25)
#main("test2024.txt",25)
main("input.txt",75)