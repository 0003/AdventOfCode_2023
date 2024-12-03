#wip
import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
p = re.compile(pattern)

do_pattern = r"do\(\)"
do_p = re.compile(do_pattern)

dont_pattern = r"don't\(\)"
dont_p = re.compile(dont_pattern)


def do_check(lookup_dict,ix):
        #check to see if max key is TRUE and that the ix is beyond
    if ix not in lookup_dict.keys():
        if lookup_dict[max(lookup_dict.keys())] and ix >= max(lookup_dict.keys()):
            return True
    else:
        return lookup_dict[ix]

def make_lookup_dict(dos,donts):
    lookup = {}                    ############### do this


def get_input(f):
    with open(f"2024/3/{f}") as fi:
        li = [x for x in  fi]
        return li  

def main(f):
    li = get_input(f)
    s = ''.join(li)

    sums_of_muls = 0
    switch = True

    muls = list(p.finditer(s))
    dos = list(i.span()[0] for i in do_p.finditer(s))
    donts = list(i.span()[0] for i in dont_p.finditer(s))

    for mul in muls:
        print(mul)
        if do_check(dos,donts,mul.span()[0],switch):
            m = int(mul.group(1)) * int(mul.group(2))
            sums_of_muls += m
            print(f"{mul.group(0)} = {m} : {sums_of_muls}")

    return sums_of_muls

main('test.txt')
#main('input.txt')

"""
Dont work
139619281
"""