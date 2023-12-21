'''--- Day 10: Pipe Maze ---'''
#works
import collections
from aoc_tools import *

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
        if i>len(a)-1 or i<0 or j>len(a[0])-1  or j<0:
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

def generate_connections(connections):
    #takes just one ij tuple, then puts them in a set, iterates it into i,j and then adds the inverse to the set.
    extended_connections = set(connections)
    for i, j in connections:
        inverse = (-i, -j)
        extended_connections.add(inverse)
    return extended_connections

def valid_pipe_connection(a,ci,cj,ni,nj,b):
    # We know S is a valid pipe so it must make a valid loop
    #A pipe connects if either both share an i or a j direction (absolute values)

    c = a[ci][cj]
    n = a[ni][nj]
    #check for ground.
    if c !=GROUND[0] and n !=GROUND[0] and b[ni][nj] == 0 and b[ni][nj] != "S":
        r = symbol_relation(a,ci,cj,ni,nj)
        n_directions = PIPE_D[n]
        c_directions = generate_connections(PIPE_D[c])
        if r in n_directions and r in c_directions:
            print(f'{c} at i: {ci} and j: {cj} and {n} at i: {ni} and j: {nj} are valid pipe conns because their relation {r} is in {n}\'s {n_directions} and {c}\'s {c_directions}  ')
            return True
        else:
            print(f'{c} at i: {ci} and j: {cj} and {n} at i: {ni} and j: {nj} are NOT valid pipe conns because their relation {r} is NOT in {n}\'s {n_directions} and {c}\'s {c_directions}  ')
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

# This is the main part 2 function 

def is_point_inside_loop_simple(oij, pipe_loop_ijs,a) -> bool:
    oi, oj = oij
    symbol_testing = a[oi][oj]
    inside = True

    count_d = collections.Counter()

    ray_casted_pipe = []
    selected_ray_casted_pipe = []
    for i in pipe_loop_ijs:
        if i[1] > oj and i[0] == oi:
            sym = a[ i[0]] [i[1] ] 
            ray_casted_pipe.append(sym) #debugging
            if sym in "|F7LJ":
                count_d[ sym ] +=1
                selected_ray_casted_pipe.append(sym) #debugging
            
    pipe_crosses = 0
    special_crosses = 0

    skip_i = False
    for i in range(len(selected_ray_casted_pipe)):
        char = selected_ray_casted_pipe[i]
        if skip_i == True:
            #this should only occur if we pulled an edge character, there was another edge character that we should skip
            skip_i = False
            continue
        elif char == "|":
            pipe_crosses += 1
            skip_i = False
        elif char in "FJL7":
            if i + 1 >= len(selected_ray_casted_pipe):
                return  False # note a closed loop so this should never happen
                break                            
            else:                
                next_two_syms = selected_ray_casted_pipe[i] + selected_ray_casted_pipe[i + 1]
                if next_two_syms in ("FJ","F7","JL","7F", "L7","LJ"): #some of these are redundant
                    special_crosses += 1
                    skip_i =  True
        
        #if there is a lone edge case then I think it's not a closed loop.
    if  not (pipe_crosses % 2 != 0 and special_crosses % 2 == 0 and pipe_crosses > 0) : #even
        inside = False
    else:
        inside == False
   
    print(f"{symbol_testing} at {oij} we looked at {''.join(ray_casted_pipe)} \
          selected { ''.join(selected_ray_casted_pipe)}, which had {pipe_crosses + special_crosses} crosses so inside = {inside}")
 
    
    return inside
    
def find_s_symbol(ij,a):
    #neighbors should just use DIRECTIONS but..
    Si, Sj = ij

    #relations
    top =  (Si - 1, Sj)
    bottom = (Si + 1, Sj)
    left = (Si , Sj - 1)
    right = (Si , Sj + 1)

#this is in opposite order
    s_directions = [(1,0), (-1,0), (0,-1),(0,1)]

    #GET THE RELATION FFROM ABOVE and CHECK IF THE NEIGHBOR SUMBOL MATCHES IT. SO S7  has relation (0,1) and a 7 has (0,1) in its Pipe_D
    neighbors_ijs = [top, bottom, left, right]
    connecting_neighbors = [False,False,False,False]

    for i in range(len(neighbors_ijs)):
        ni, nj = neighbors_ijs[i]
        ns = a[ni][nj]

        if not valid_cell(a,ni,nj):
            continue # this is either out of range our a "."
        nr_set = set()
        for nr in PIPE_D[ns]:
            nr_set.add(nr) ###ned to figure this out
        dir_set = set( [s_directions[i]])

        intersection = nr_set & dir_set
        if intersection:
            connecting_neighbors[i] = True
                                #top bot    left  right
    if connecting_neighbors == [True, True, False, False]:
        s_symbol = "|"
    elif connecting_neighbors == [True, False, True, False]:
        s_symbol = "J"
    elif connecting_neighbors == [True, False, False, True]:
        s_symbol = "L"
    elif connecting_neighbors == [False, False, True, True]:
        s_symbol = "-"
    elif connecting_neighbors == [False, True, False, True]:
        s_symbol = "F"
    elif connecting_neighbors == [False, True, True, False]:
        s_symbol = "7"
    else:
        raise Exception("Should not happen")

    print(f"{MAGENTA_AOCTOOLS} S is a {s_symbol} {RESET_AOCTOOLS}")

    return s_symbol
    

def get_count_of_os(b,a,sij) -> int:
    ############# for each o race trace against
    Si, Sj = sij
    s_sym= find_s_symbol(sij,a)
    string_s = a[Si]
    string_s = string_s[:Sj] + s_sym + string_s[Sj + 1:]
    a[Si]= string_s

    pipe_loop_ijs = [] 
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == "S":
                pipe_loop_ijs.append((i, j))
            elif b[i][j] > 0:
                pipe_loop_ijs.append((i, j))

    #pipe_loop_ijs = sort_loop(pipe_loop)
    #pipe_loop_ijs = extract_vertices(pipe_loop_ijs)
    
    d = [['*']*len(a[0]) for _ in range(len(a))]
    aa = [['*']*len(a[0]) for _ in range(len(a))]

    count = 0
     
    for i in range(len(a)):
        for j in range(len(a[0])):
            oij = (i,j)
            if oij not in pipe_loop_ijs :
                if is_point_inside_loop_simple(oij,pipe_loop_ijs,a):
                #if is_point_inside_loop(oij,pipe_loop_ijs):
                    count += 1
                    d[i][j] = f"{RED_AOCTOOLS}{b[i][j]}{RESET_AOCTOOLS}"
                    aa[i][j] = f"{RED_AOCTOOLS}{a[i][j]}{RESET_AOCTOOLS}"
                else:    
                    d[i][j] = f"{GREEN_AOCTOOLS}{b[i][j]}{RESET_AOCTOOLS}"
                    aa[i][j] = f"{GREEN_AOCTOOLS}{a[i][j]}{RESET_AOCTOOLS}"
            else:
                d[i][j] = f"{BLUE_AOCTOOLS}{b[i][j]}{RESET_AOCTOOLS}"
                aa[i][j] = f"{BLUE_AOCTOOLS}{a[i][j]}{RESET_AOCTOOLS}"

    for i in range(len(a)):
        for j in range(len(a[0])):
            if d[i][j] == "*": #should not hit
                d[i][j] = f"{YELLOW_AOCTOOLS}{b[i][j]}{RESET_AOCTOOLS}"
                aa[i][j] = f"{YELLOW_AOCTOOLS}{a[i][j]}{RESET_AOCTOOLS}"
            if (i,j) in pipe_loop_ijs:
                d[i][j] = f"{MAGENTA_AOCTOOLS}{b[i][j]}{RESET_AOCTOOLS}"
                aa[i][j] = f"{MAGENTA_AOCTOOLS}{a[i][j]}{RESET_AOCTOOLS}"

    print_2darrays_side_by_side(d,aa,a1_has_ansi=True, a2_has_ansi=True) #since d has ANSI colors need to do this to make it print okay
    return count

""" Utility Functions """
#Using AOC_Tools

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
    bbb = [[0]*len(a[0]) for _ in range(len(a))]
    b[s_tup[0]][s_tup[1]] = "S"
    c = ['~'*len(a[0]) for _ in range(len(a))]
    aaa = [[0]*len(a[0]) for _ in range(len(a))]
    s_loop_ijs = set()

    stop_flag = False
    while steps < (len(a) * len(a[0])) or stop_flag: #this represents searching every space
        steps += 1
        next_positions = []
        for cij in cursor_positions:
            ci,cj = cij
            nexts = get_neighbors(a,ci,cj,b)
            next_positions.extend(nexts)
            for n in next_positions:
                b[n[0]][n[1]]  = steps
                bbb[n[0]][n[1]] = f"{MAGENTA_AOCTOOLS}{steps}{RESET_AOCTOOLS}" # to check
                aaa[n[0]][n[1]] = f"{MAGENTA_AOCTOOLS}{a[n[0]][n[1]]}{RESET_AOCTOOLS}"

                s_loop_ijs.add( (n[0], n[1]) )
                c[n[0]] = ''.join(map(str, b[n[0]]))  #this is broken
            #print_map(c,a)
            print_2darrays_side_by_side(bbb,a,a1_has_ansi=True,a2_has_ansi=True)
            if s_tup not in nexts:
                print(f"steps {steps}")
                cursor_positions = next_positions
            else:
                stop_flag = True
                print(f"Total steps {steps}.")
                print("~~~~~PRINTING FINAL MAP~~~~")
                return
    print(f"Total steps {steps}.")
    print("~~~~~PRINTING FINAL MAP~~~~")
    #print_map(c,a)
    print_2darrays_side_by_side(b,a)
    furthest_step  = 0
    for row_vs in b:
        for col_v in row_vs:
            if col_v != "S":
                furthest_step = max(col_v,furthest_step)
    print(f"furtherst step: {furthest_step}")

    print(f"{RED_AOCTOOLS} STARTING  PART TWO {RESET_AOCTOOLS}")

    count = get_count_of_os(b,a,s_tup)
    print(f"counts = {count}")
    return count


def tests():
    """---------------  Part 2 tests ---------------------------"""
    #main('10/2test1.txt',"first test")
    #main('10/2test2.txt',"second test")
    #main('10/2test3.txt',"third test")
    #main("10/spiral.txt","spiral") #works
    #main('10/2testw1.txt', "making the pip be narroweer")
    #main('10/2testw2.txt', "making the pip be narroweer and with junk")
    main('10/upanddown.txt', "trying to test if my pipe loop works -- this is the key test")

def part_2():   
    main('10/input.txt',"NA")

tests()
    
#part_2()





