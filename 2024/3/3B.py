#wip
import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
p = re.compile(pattern)

do_pattern = r"do\(\)"
do_p = re.compile(do_pattern)

dont_pattern = r"don't\(\)"
dont_p = re.compile(dont_pattern)


def do_check(lookup_dict,ix,dos,donts):
        #check to see if max key is TRUE and that the ix is beyond
    if ix not in lookup_dict.keys():
        if ix >= dos[-1] > donts[-1]:
            return True
        else:
            return False
    else:
        return lookup_dict[ix]

def make_lookup_dict(dos,donts):
    dos = [0] + dos
    lookup = {}                   ############### do this
    i, j = 0, 0
    current = None

    while i < len(dos) or j < len(donts):
          #have a good do  and #donts out      OR    #dont has not come up
          #should not happen oftent
        if i < len(dos) and (j >= len(donts) or dos[i] <= donts[j]):
            current = dos[i]
            i += 1
        #main driver go until you hit a dont
        elif j < len(donts):
            if current is not None:
                for x in range(current,donts[j] + 1):
                    lookup[x] = True
                current = None
            j += 1
    return lookup

def get_input(f):
    with open(f"2024/3/{f}") as fi:
        li = [x for x in  fi]
        return li  

def main(f):
    li = get_input(f)
    s = ''.join(li)

    sums_of_muls = 0

    muls = list(p.finditer(s))
    dos = list(i.span()[0] for i in do_p.finditer(s))
    donts = list(i.span()[0] for i in dont_p.finditer(s))
    lookup = make_lookup_dict(dos,donts)

    for mul in muls:
        print(mul)
        if do_check(lookup,mul.span()[0],dos,donts):
            m = int(mul.group(1)) * int(mul.group(2))
            sums_of_muls += m
            print(f"{mul.group(0)} = {m} : {sums_of_muls}")
    print(len(s))
    print(lookup)
    print(sums_of_muls)
    return sums_of_muls

#main('test1.txt')
#main('test2.txt')
main('input.txt')

"""
Dont work
139619281
22485852
"""