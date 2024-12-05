#works

def print_map(li):
    for i in li:
        print(i)

def find_x_mas(li,i,j):
    char = li[i][j]
    if char != "A":
        return 0
    #mtop  
    elif li[i-1][j-1] == "M" and li[i-1][j+1] == "M" and li[i-1][j-1] == "M" and li[i-1][j+1]

    

    #mbottom

    #M-side-S

    #S-side-M

def count_phrase(li,phrase):
    counts = 0
    for _,i in enumerate(li):
        matches = p.findall(i)
        if len(matches) > 0:
            counts += len(matches)
    
    return counts

def get_input(f):
    with open(f"2024/4/{f}") as fi:
        li = ["0" + x.strip() + "0" for x in fi]
        padding = "0" * len(li[0])
        li = [padding] + li + [padding]
        return li

def main(f):
    li = get_input(f)
    print_map(li)


main("testb.txt")
#main('input.txt')
