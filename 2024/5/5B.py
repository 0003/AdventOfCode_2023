#working
from collections import defaultdict
import re

#dict keys must come before values
rules = defaultdict(list)

rule_pattern = r"(\d+)\|(\d+)"

updates = []
invalid_updates = []
fixed_updates = []

def fix_update(update,rules):
    trigger = True
    while trigger:
        trigger = False
        for i, n in enumerate(update):
            for value in update[:i]:
                if value in rules[n]:
                    trigger = True
                    update.remove(value)
                    update.insert(i,value)
                    #print(f"New Update = {update}")
                    break
            if trigger:
                break
    return update
                


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
        if not test_update(update,rules):
            
            invalid_updates.append(update)
            fixed_update = fix_update(update,rules)
            fixed_updates.append(fixed_update)
            middle = get_middle(fixed_update)
            score += middle
            print(f"{update} was invalid. But is now {fixed_update} The {middle = } {score = }")
    print(f"{score = }")
    return

#main("test.txt")
main("input.txt")