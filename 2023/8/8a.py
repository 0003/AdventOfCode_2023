"""--- Day 8: Haunted Wasteland ---"""
#works
import re

start = "AAA"
end = "ZZZ"

def get_input(fi):
    with open(fi) as f:
        return f.readlines()

def cycle_1d(s):
    while True:
        old = s
        s =  s[1:] + s[0]
        yield old[0]

def main(fi):
    print(f'{fi}')
    inp = get_input(fi)
    directions = inp[0].strip()
    print(directions)
    nodes = {}

    for i,e in enumerate(inp[2:]):
        p = re.compile(r'[A-Z]{3}')
        n,l,r = p.findall(e)
        nodes[n] = (l,r)

    count = 0
    next_node = start
    for d in cycle_1d(directions):
        count += 1
        #d is the directions string cycled. We grab the first digit
        l_r = lambda x: 0 if x == "L" else 1
        next_node = nodes[next_node][l_r(d)]
        if next_node == end:
            break

    print(count)
    return count

main('8/test.txt')
main('8/test2.txt')
main('8/input.txt')