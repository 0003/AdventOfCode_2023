#works
from termcolor import colored

def print_grid(grid,i=None,j=None):
    print(f"\n{(i,j) = }")
    if i is None and j is None:
        for row in grid:
            print(row)
    else:
        for ix, row in enumerate(grid):
            for jx, char in enumerate(row):
                if i == ix and j == jx:
                     print(colored(char,"red"), end="")
                else:
                    print(char,end="")
            print("")

def get_num(grid,i,j):
    char = grid[i][j]
    if char in ("X","."):
        return 9999
    return int(char)

def can_move(grid, loc : tuple, cursor_num):
    i, j = loc[0], loc[1]
    #print_grid(grid,i,j)
    char = grid[i][j]
    if char in  ("X", "."):
        return False
    
    elif int(char) - cursor_num == 1:
        print(f"Destination {int(char) = } is one less than {cursor_num = }")
        return True
    
    else:
        return False

def climb(grid, cursor : tuple):
    tops = []
    cursor_num = get_num(grid,cursor[0],cursor[1]) #should be always zero for part 1
    possible_nexts = [cursor]
    
    visited = set()
    while possible_nexts:
        cursor = possible_nexts.pop()
        cursor_num = get_num(grid,cursor[0],cursor[1])
        i , j = cursor[0], cursor[1]
        next_north = (i - 1, j)
        next_south = (i + 1 , j)
        next_east  = (i, j + 1)
        next_west  = (i, j - 1)

        next_moves = [next_north, next_east, next_south, next_west]
        valid_moves = []
        for next_move in next_moves:
            visited.add(next_move) 
            print(f"New start: {next_move = } ")
            if can_move(grid, next_move, cursor_num):
                valid_moves.append( (next_move, get_num(grid,next_move[0],next_move[1])))
                print(colored(f"{next_move =} which is {get_num(grid,next_move[0],next_move[1])} is valid bc its 1 more than {get_num(grid,i,j)}","green"))

                if get_num(grid,next_move[0],next_move[1]) == 9:
                    tops.append(next_move)
                    continue 
                possible_nexts.append(next_move)      
    return tops
            
def find_chars(grid,target_char="0"):
    char_ijs = []
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == target_char:
                char_ijs.append((i,j))
    return char_ijs


def get_input(f):
    with open(f"2024/10/{f}") as fi:
        grid = ["X" + e.strip() + "X" for e in fi]
        grid = ["X" * len(grid[0])] + grid + ["X" * len(grid[0])] 
        return grid

def main(f):
    grid = get_input(f)
    print_grid(grid)
    starts = find_chars(grid,"0")
    
    trails_score = 0
    valid_trails = set()
    for start in starts:
        print(f"Climbing from {start = } and there are {valid_trails = }")
        trails_ = climb(grid,start)
        for end in trails_:
            if (start,end) not in valid_trails:
                valid_trails.add((start,end))
        print(f"{trails_ =}")
        print(f"{valid_trails = }")
        trails_score += len(trails_)
    print(f"Final {trails_score = }")

#main('test.txt')
#main('test1.txt')
#main('test2.txt')
#main('testB1.txt')
#main('testB2.txt')
main('input.txt')