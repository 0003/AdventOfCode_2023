#works
import string

def print_map(li):
    for i in li:
        print(i)

def get_input(f):
    with open(f"2024/6/{f}") as fi:
        map = ["0" + x.strip() + "0" for x in fi]
        padding = "0" * len(map[0])
        map = [padding] + map + [padding]
        return map

def main(f):
    map = get_input(f)
    print_map(map)

    path = []
    travel_map = [c for c in map]

    for i, row in enumerate(map):
        for j, char in enumerate(row):
            if char == "^":
                cursor = (i,j)
                direction = (-1,0) #north
                path.append(cursor)

    exit = False
    while not exit:
        i, j = cursor[0], cursor[1]
        i_prime, j_prime = i + direction[0], j + direction[1]
        next_loc = map[i_prime][j_prime]

        if next_loc == "0":
            exit = True
            travel_map[i] = travel_map[i][:j] + "!" + travel_map[i][j+1:]
            print_map(travel_map)
            print(f"{len(path) = }")  

        elif next_loc == "#":
            if direction == (-1,0):
                direction = (0,1) 
            elif direction == (0,1):
                direction = (1,0) 
            elif direction == (1,0):
                direction = (0,-1) 
            elif direction == (0,-1):
                direction = (-1,0) 
        else:
            if next_loc == "." or next_loc == "^":
                cursor = (i_prime, j_prime)
                if cursor not in path:
                    path.append(cursor)
                travel_map[i] = travel_map[i][:j] + string.ascii_uppercase[(len(path) - 1 )% len(string.ascii_uppercase)] + travel_map[i][j+1:]

    return path

#main('test.txt')
main("input.txt")
