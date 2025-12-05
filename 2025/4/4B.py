import pprint

DIRECTIONS =[(0,1), #right
             (0,-1), #left
             (1,0), #down
             (-1,0), #up
             (1,1), #down-right
             (1,-1), #down-left
             (-1,1), #up-right
             (-1,-1)#up-left
            ]

def check(row,col,arr):
    counts = 0
    for tup in DIRECTIONS:
        if arr[row+tup[0]][col+tup[1]] == "@":
            counts += 1
    if counts < 4:
        return True
    else:
        return False


def main(f):
    with open(f) as fi:
        lines = [line.strip() for line in fi]
        width = len(lines[0])+2
        border = "U" * width
        lines = [border] + [f"U{line}U" for line in lines] + [border]
        lines = [list(line) for line in lines]
        #pprint.pprint(lines)
    count = 0
    updates = []
    toggle = True
    while toggle:
        updates = []
        for row_ix,row_str in enumerate(lines):
            for col_ix,char_s in enumerate(row_str):
                if char_s == "@":
                    if check(row_ix,col_ix,lines):
                        count += 1
                        updates.append((row_ix,col_ix))
        for update in updates:
            lines[update[0]][update[1]] = "X"
        if updates == []:
            toggle = False

    for line in lines:
        print(''.join(line),sep="")
    print(f"{count = }")




#main("2025/4/test.txt")
main("2025/4/input.txt")