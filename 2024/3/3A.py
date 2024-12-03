#works
import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
p = re.compile(pattern)


def get_input(f):
    with open(f"2024/3/{f}") as fi:
        li = [x for x in  fi]
        return li  


def main(f):
    li = get_input(f)
    print(len(li))

    sums_of_muls = 0
    for line in li:
        muls = p.findall(line)
        for mul in muls:
            m = int(mul[0]) * int(mul[1])
            
            sums_of_muls += m
            print(f"{mul[0]} X {mul[0]} = {m} : {sums_of_muls}")

    return sums_of_muls

#main('test.txt')
main('input.txt')