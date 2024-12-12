#works
def blink(stones):
    new_stones = []

    for i, stone in enumerate(stones):
        chars = str(stone)
        if stone == 0:
            stone = 1
        elif len(chars) % 2 == 0:
            ix = (len(chars) // 2)
            stone_a = int(chars[:ix])
            stone_b = int(chars[ix:])
            stone = (stone_a, stone_b)      
        else:
            stone *= 2024

        if isinstance(stone,tuple): 
            new_stones.extend(stone)
        elif isinstance(stone,int): 
            new_stones.append(stone)
    
    return new_stones


def get_input(f):
    with open(f'2024/11/{f}') as fi:
        stones = [int(e) for line in fi.readlines() for e in line.split(" ")]
        print(stones)
        return stones

def main(f):
    stones = get_input(f)
    for i in range(25):
        stones = blink(stones)
        print(f"Blinks = {i+1}",stones, f"{len(stones) = }")

    print(f"{len(stones) = }")
    return stones

main("test.txt")
#main("input.txt")