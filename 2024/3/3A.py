import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
context_pattern = r"(do\(\))?|(do\(\))?.*
p = re.compile(pattern)
context_p = re.compile(context_pattern, re.DOTALL)

def get_input(f):
    with open(f"2024/3/{f}") as fi:
        li = [x for x in fi]
        return li

def main(f):
    li = get_input(f)
    print(f"Number of lines: {len(li)}")

    sums_of_muls = 0
    s = "".join(li)  # Combine all lines for context matching
    contexts = context_p.findall(s)  # Extract segments between boundaries

    for context in contexts:
        muls = p.findall(context)  # Find mul() instances in each context
        for mul in muls:
            m = int(mul[0]) * int(mul[1])
            sums_of_muls += m
            print(f"{mul[0]} X {mul[1]} = {m} : {sums_of_muls}")

    return sums_of_muls

main('test1.txt')
#main('test2.txt')
#main('input.txt')
