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

def get_target_index_in_list(tgt : int, li : list[int]): #coould make bisect here but day 3 
    inlist = False
    closest_ix = 0
    for i, e in enumerate(li):
        if e < tgt:
            inlist = True
            closest_ix = e
    return (inlist, closest_ix )

def do_check(mul,dos,donts):
    mulix = mul.span()[0]
    dosix =  get_target_index_in_list(mulix,dos) #index or None
    dontsix = get_target_index_in_list(mulix,donts) #index or None
    
    if dosix[0]:
        return



def get_input(f):
    with open(f"2024/3/{f}") as fi:
        li = [x for x in  fi]
        return li  

def main(f):
    li = get_input(f)
    s = ''.join(li)
    print(f"{len(s) = } which should be 1")

    sums_of_muls = 0
    muls = list(p.finditer(s))
    dos = [0] + list(i.span()[0] for i in do_p.finditer(s))
    donts = list(i.span()[0] for i in dont_p.finditer(s))

    for mul in muls:
        #print(mul)
        if do_check(mul,dos,donts):
            m = int(mul.group(1)) * int(mul.group(2))
            sums_of_muls += m
            print(f"{mul.group(0)} = {m} : {sums_of_muls}")
    print(len(s))
    print(sums_of_muls)
    return sums_of_muls

#main('test1.txt')
#main('test2.txt')
#main('test.txt')

main('input.txt')

"""
Dont work
139619281
22485852
"""