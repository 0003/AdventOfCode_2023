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

# This is the main part 2 function It needs an ordered list of pipe tuples

def is_point_inside_loop_simple(oij, pipe_loop_ijs,a) -> bool:
    oi, oj = oij
    inside = False

    #probably going to have to logic this out.

    #need to do a check on borders
    pipe_ijs_for_crossing_bottom =  set([i[0] for i in pipe_loop_ijs if i[0] > oi and i[1] == oj and a[i[0]][i[1]] not in "-LJ" ])
    pipe_ijs_for_crossing_top = set([i[0] for i in pipe_loop_ijs if i[0] < oi and i[1] == oj and a[i[0]][i[1]] not in "-LJ"])
    pipe_ijs_for_crossing_right = set([i[1] for i in pipe_loop_ijs if i[1] > oj and i[0] == oi and a[i[0]][i[1]] not in "|F7"])
    pipe_ijs_for_crossing_left = set([i[1] for i in pipe_loop_ijs if i[1] < oj and i[0] == oi and a[i[0]][i[1]] not in "|F7" ])

    crosses = [pipe_ijs_for_crossing_bottom,pipe_ijs_for_crossing_top, pipe_ijs_for_crossing_right,pipe_ijs_for_crossing_left]
    cross_counts = [len(c) for c in crosses]
    median_cross_count =  sorted(cross_counts,reverse=True)[1] #median rounding to the most
    print(f'oij: {oij} crossed this many times: {cross_counts}')

    if median_cross_count % 2 == 0:
        return 0
    else:
        return 1
    

def is_point_inside_loop(oij, pipe_loop_ijs) -> bool:
    oi, oj = oij
    inside = False

    for ix in range(len(pipe_loop_ijs)):
        i1, j1 = pipe_loop_ijs[ix]
        i2, j2 = pipe_loop_ijs[(ix + 1) % len(pipe_loop_ijs)]

        if oj > min(j1, j2) and oj < max(j1, j2) and oi < max(i1, i2):
            if j1 != j2:
                #https://youtu.be/RSXM9bgqxJM?si=wd6XCVyH161i2BPy&t=207
                #----------(x1) + ----(i_inters)/
                i_inters = i1 + ( (oj - j1) * ((i2 - i1) / (j2 - j1)) ) 
            # I think this will always bee the case but coding out all of this
                #also if i1 == i1 then the intercept portion of i to add is zero
            if i1 == i2 or oi < i_inters:
                #first hit is odd number so since we begin with False, it returns true on odd hits
                inside = not inside  
    return 1


def sort_loop(points): #this runs in n log n time I think
    if not points:
        return []
    #create a dictionary mapping points to their adjacent points
    def create_adjacency_dict(points):
        adj_dict = {}
        for point in points:
            i, j = point
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                adjacent = (i + di, j + dj)
                if adjacent in points:
                    adj_dict.setdefault(point, set()).add(adjacent) #this is a key coding pattern. use more often
        return adj_dict

    points_set = set(points) #probably not needed 
    adj_dict = create_adjacency_dict(points_set)

    sorted_loop = [points[0]]
    points_set.remove(points[0])

    # Build the sorted loop
    while points_set:
        last_point = sorted_loop[-1]
        next_points = adj_dict.get(last_point, set())
        intersection = next_points.intersection(points_set)
        
        # Check if the intersection is not empty
        if intersection: #this was a bug before
            next_point = intersection.pop()
        else:
            next_point = None
        if not next_point:
            break

        sorted_loop.append(next_point)
        points_set.remove(next_point) #key to do

    return sorted_loop


def extract_vertices(pipe_loop_ijs): # should be linear time
    """ This just reduces the space"""
    if len(pipe_loop_ijs) < 3:  # If there are less than 3 points, all are vertices. Just in case I want to test more or use later
        return pipe_loop_ijs

    vertices = [pipe_loop_ijs[0]]  # Start with the first point

    for ix in range(1, len(pipe_loop_ijs) - 1): #because we already pull one out
        prev_i, prev_j = pipe_loop_ijs[ix - 1]
        i, j = pipe_loop_ijs[ix]
        next_i, next_j = pipe_loop_ijs[(ix + 1) % len(pipe_loop_ijs)] #cycling at the end

        if (i != prev_i and i != next_i) or (j != prev_j and j != next_j):
            vertices.append((i, j))

    vertices.append(pipe_loop_ijs[-1])  # Add the last point

    return vertices


def get_count_of_os(b,a,search_space) -> int:
    ############# for each o race trace against
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
     
    """for i in search_space[0]:
        for j in search_space[1]:"""
    
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
            if d[i][j] == "*":
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
    b[s_tup[0]][s_tup[1]] = "S"
    c = ['~'*len(a[0]) for _ in range(len(a))]

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
                b[n[0]][n[1]] = steps # to check
                s_loop_ijs.add( (n[0], n[1]) )
                c[n[0]] = ''.join(map(str, b[n[0]]))  #this is broken
            #print_map(c,a)
            #print_2darrays_side_by_side(b,a)
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
    #search space we will find the min and max of i's and j's on the loop
    s_loop_min_i = min(e[0] for e in s_loop_ijs)
    s_loop_max_i = max(e[0] for e in s_loop_ijs)
    s_loop_min_j = min(e[1] for e in s_loop_ijs)
    s_loop_max_j = max(e[1] for e in s_loop_ijs)

    search_space =(range(s_loop_min_i , s_loop_max_i + 1), range(s_loop_min_j, s_loop_max_j + 1) )

    count = get_count_of_os(b,a,search_space)
    print(f"counts = {count}")
    return count


def tests():
    """---------------  Part 2 tests ---------------------------"""
    #main('10/2test1.txt',"first test")
    #main('10/2test2.txt',"second test")
    #main('10/2test3.txt',"third test")
    #main('10/2testw1.txt', "making the pip be narroweer")
    main('10/2testw2.txt', "making the pip be narroweer and with junk")

def part_2():   
    main('10/input.txt',"NA")

tests()
    
#part_2()





