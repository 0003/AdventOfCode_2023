
dp = {}

def design_possible(design : str,towels : set):
    if design not in dp:
        if len(design) == 0:
            return 1
        else:
            res = 0
            for t in towels:
                if design.startswith(t):
                    res += design_possible( design[len(t):], towels )
            dp[design] = res
    return dp[design]
            

def get_input(f):
    with open(f"2024/19/{f}") as fi:
        lines =  fi.readlines()
        towels = [e.strip() for e in lines[0].split(",")]
        designs =  [e.strip() for e in lines[2:]]
        
        return (towels, designs)

def main(f):
    towels, designs = get_input(f)
    towels = set(towels)
    score = 0
    for design in designs:
        score += design_possible(design, towels)
        print(f"{ design = } {score = }" )

    print(f"{score = }")
    return

#main("test1.txt")
#main("test.txt")

main("input.txt")