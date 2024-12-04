#works
import re
from collections import defaultdict

phrase = "XMAS"

def print_map(li):
    for i in li:
        print(i)

def count_phrase(li,phrase):
    p = re.compile(phrase)
    counts = 0
    for _,i in enumerate(li):
        matches = p.findall(i)
        if len(matches) > 0:
            counts += len(matches)
    
    return counts

def rotate_90(li):
    li_prime = []
    for j,_ in enumerate(li[0]):
        string = ""
        for i,_ in enumerate(li):
            string += li[i][j]
        li_prime.append(string)

    print(f"Rotated 90:")
    print_map(li_prime)
    
    return li_prime

def rotate_45(li):
    diagonals = defaultdict(list)

    for i,_ in enumerate(li):
        for j,_ in enumerate(li[0]):
            char = li[i][j]
            diagonals[i + j].append(char)
    
    keys = sorted(diagonals.keys(),reverse=True)
    li_prime = [''.join(diagonals[k]) for k in keys]

    print(f"Rotated 45:")
    print_map(li_prime)

    return li_prime


def rotate_315(li):
    diagonals = defaultdict(list)

    for i,_ in enumerate(li):
        for j,_ in enumerate(li[0]):
            char = li[i][j]
            diagonals[i - j].append(char)
    
    keys = sorted(diagonals.keys(),reverse=True)
    li_prime = [''.join(diagonals[k]) for k in keys]

    print(f"Rotated 315:")
    print_map(li_prime)

    return li_prime


def get_input(f):
    with open(f"2024/4/{f}") as fi:
        li = [x.strip() for x in fi]
        return li

def main(f):
    li = get_input(f)
    print_map(li)
    counts = 0
    #left to right
    counts += count_phrase(li,phrase)
    #right to left
    counts +=count_phrase(li,phrase[::-1])
    print(f"Horizontal Counts: {counts}")

    print(f"Rotating 90 for Vertical counts")
    li_90 = rotate_90(li)
    counts += count_phrase(li_90,phrase)
    counts += count_phrase(li_90,phrase[::-1])
    print(f"Vertical Counts: {counts}")

    print(f"Rotating 45 for Diag part A counts")
    li_45 = rotate_45(li)
    counts += count_phrase(li_45,phrase)
    counts += count_phrase(li_45,phrase[::-1])
    print(f"45 deg Counts: {counts}")

    print(f"Rotating 315 for Diag part B counts")
    li_315 = rotate_315(li)
    counts += count_phrase(li_315,phrase)
    counts += count_phrase(li_315,phrase[::-1])
    print(f"315 deg Counts: {counts}")

    print(f"Final Counts: {counts}")
    return counts


#main('test1.txt')
#main("test2.txt")
main('input.txt')
