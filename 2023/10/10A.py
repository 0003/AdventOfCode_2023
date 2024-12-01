'''--- Day 10: Pipe Maze ---'''
#works
import collections

PIPES = '|-FJL7S' #make sure code is case sensitive
GROUND = '.' #cant be in pipe and ground

DIRECTIONS = [(1,  0), # up receive up 
             ( -1,  0), # Down  
             ( 0, 1), # Left
             ( 0, -1)] # right

PIPE_D = {"|": (DIRECTIONS[0], DIRECTIONS[1]), # | up  (-1,  0) and down ( 1,  0)
          "-": (DIRECTIONS[2], DIRECTIONS[3]), #_ left  ( 0, -1) and right ( 0,  1)
          "F": (DIRECTIONS[1], DIRECTIONS[3]), # F down ( 1,  0) and right ( 0,  1)
          "J": (DIRECTIONS[0], DIRECTIONS[2]), #J up (-1,  0) and left ( 0, -1)
          "L": (DIRECTIONS[0], DIRECTIONS[3]),#L up (-1,  0)  and right ( 0,  1)
          "7": (DIRECTIONS[1], DIRECTIONS[2]), #7 down ( 1,  0) and left ( 0, -1)
          "S": set(DIRECTIONS) #S ALL that are valid?                                
          }

""" Operation Methods"""
def symbol_relation(a,ci,cj,ni,nj) -> tuple:
    #this is their relation ni - ci, nj -ci
    c = PIPE_D[a[ci][cj]] #direction tuple
    n = PIPE_D[a[ni][nj]]
    if ni > ci: #Bigger index means you need to add +1 to C
        r = (1 , 0)
    elif ni < ci: #smaller index means you need to subtractt 1
        r = (-1, 0)
    elif nj > cj: #bigger mean yoy need to add 1 to cj to move right
        r = (0, 1)
    elif nj < cj: #smaller means you need to subtract 1 to cj to move left
        r = (0, -1)
    else:
        raise Exception("Should not happen")
    return r

def get_starting_location(a) -> tuple:
    assert isinstance(a[0][0],str), f"Element at index ({i}, {j}) is not a string."
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == "S":
                print(f"S characer found at i: {i} J: {j}")
                return(i,j)
    return None

def valid_cell(a,i,j) -> bool:
    """Use with get_neighbors to check if a loc is out of range"""
    try:
        if i>len(a)-1 or i<0 or j>len(a[0]) or j<0:
            #print(f' i: {i} j: {j} {a[i][j]} is not valid cell')
            return False
        elif a[i][j] == ".":
            #print(f' i: {i} j: {j} {a[i][j]} is not valid cell')
            return False
        else:
            #print(f' i: {i} j: {j} {a[i][j]} is a valid cell')
            return True
    except IndexError:
        return False
    
def valid_pipe_connection(a,ci,cj,ni,nj,b):
    # We know S is a valid pipe so it must make a valid loop
    #A pipe connects if either both share an i or a j direction (absolute values)

    c = a[ci][cj]
    n = a[ni][nj]
    #check for ground.
    if c !=GROUND[0] and n !=GROUND[0] and b[ni][nj] == 0 and b[ni][nj] != "S":
        r = symbol_relation(a,ci,cj,ni,nj)
        n_directions = PIPE_D[n]
        if r in n_directions:
            print(f'{c} at i: {ci} and j: {cj} and {n} at i: {ni} and j: {nj} are valid pipe conns because their relation {r} is in {n}\'s {n_directions} ')
            return True
        else:
            print(f'{c} at i: {ci} and j: {cj} and {n} at i: {ni} and j: {nj} are NOT valid pipe conns because their relation {r} is NOT in {n}\'s {n_directions} ')
            return False
    else:
        print(f'{c} and {n} are not valid pipes because at least one is a "." or b[ni][nj] = {b[ni][nj]} which may be zero or S')
        return False

def get_neighbors(a,i,j,b):
    if not valid_cell(a,i,j):
        raise Exception("This cursor should never been validated")
        return []
    neighbors = [(i + d[0], j + d[1]) for d in DIRECTIONS if valid_cell(a, i + d[0],j + d[1])] # need to think about this
    valid_neighbor_cells = []
    for n in neighbors:
        ni, nj = n
        if valid_pipe_connection(a,i,j,ni,nj,b):
            bnij = b[ni][nj]
            if bnij == 0 or bnij != "S":
                valid_neighbor_cells.append(n)
    
    return valid_neighbor_cells   

""" Utility Functions """
   

""" Debug Functions """
def print_map(a,og_a,ci=None,cj=None):

    records_length = len(a)
    width_length = len(a[0])
    print("  " +''.join( str(j)[-1] for j in range(2*width_length)))
    print("  "+''.join( "V" for _ in range(2*width_length)))     
    for i in range(records_length):
        j_string = str(i) + ">"
        for j in range(width_length):
            j_string += a[i][j]
        for jj in range(width_length):
            j_string += og_a[i][jj]
        print(j_string)
    return

""" Main """
def get_input(fi):

    with open(fi) as f:
        data = [i.strip() for i in f.readlines()]
        return data
    
def main(file,comment):

    print(f"\n----------- {file} ------------------ :",comment)
    a = get_input(file)
   # print_map(a,3,1) #This test i j referencing or spotting error
    #print_map(a,a)

    #cij is a tuple of i j that is passed from function to function
    s_tup = get_starting_location(a)
    cursor_positions = [s_tup]
    
    steps = 0
    b = [[0]*len(a[0]) for _ in range(len(a))]
    b[s_tup[0]][s_tup[1]] = "S"
    c = ['~'*len(a[0]) for _ in range(len(a))]
    while steps < len(a) * len(a[0]): #this represents searching every space
        steps += 1
        next_positions = []
        for cij in cursor_positions:
            ci,cj = cij
            nexts = get_neighbors(a,ci,cj,b)
            next_positions.extend(nexts)
            for n in next_positions:
                b[n[0]][n[1]] = steps # to check
                c[n[0]] = ''.join(map(str, b[n[0]]))
            #print_map(c,a)
            if s_tup not in nexts:
                print(steps)
                cursor_positions = next_positions
            else:
                print(f"Total steps {steps}.")
                print("~~~~~PRINTING FINAL MAP~~~~")
                for row in c:
                    print(row)
                return
    print(f"Total steps {steps}.")
    print("~~~~~PRINTING FINAL MAP~~~~")
    print_map(c,a)

    furthest_step  = 0
    for row_vs in b:
        for col_v in row_vs:
            if col_v != "S":
                furthest_step = max(col_v,furthest_step)
    print(f"furtherst step: {furthest_step}")
    return furthest_step

def tests():
    #main('10/test1S.txt',"s in bottom corner")
    #print("-"*80)
   # main('10/test2.txt', "probably harder")
    #print("-"*80)
    main('days/10/test3.txt', print("hard test"))
    #print("-"*80)'''
    #main('10/testw.txt', "simple square seems to work") 
    #main('10/testw1.txt'," square with vertical and horizontals") 
    #main('10/testw2.txt'," S verticals to an S")
    #main('10/testmisc.txt',"these are scratch tests") 

def part_1():   
    main('days/10/input.txt',"NA")

#tests()
    
part_1()





