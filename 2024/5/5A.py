from collections import defaultdict
import re
import numpy as np

#dict keys must come before values
rules = defaultdict(list)

rule_pattern = r"(\d+)\|(\d+)"

updates = []
valid_updates = []

def test_update(update,rules):
    for i, n in enumerate(update):
        if any(value in rules[n] for value in update[:i]):
            return False
    return True

def get_middle(update):
    l = len(update)
    if l > 0 and 1 % 2 != 0:
        middle_ix = l // 2 
        return update[middle_ix]

def get_input(f):
    with open(f"2024/5/{f}") as fi:
        li = [x.strip()for x in fi]
        for e in li:
            rule = re.findall(rule_pattern,e)
            if len(rule)>0:
                rules[int(rule[0][0])].append(int(rule[0][1]))
            elif e == "":
                pass
            else:
                updates.append([int(i) for i in e.split(",")])
        return rules, updates

def main(f):
    rules, updates = get_input(f)
    score = 0
    for update in updates:
        if test_update(update,rules):
            
            valid_updates.append(update)
            middle = get_middle(update)
            score += middle
            print(f"{update} is valid. The {middle = } {score = }")
    print(f"{score = }")

#main("test.txt")
main("input.txt")