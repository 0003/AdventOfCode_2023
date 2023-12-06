'''--- Day 4: Scratchcards ---
'''

#works_

import re
from collections import Counter

def get_input():
    with open('4/input.txt') as f:
        a = f.readlines()
        return a
    
def parse_tickets(a):
    winnings = 0
    for i,t in enumerate(a):
        print(t)
        t += ' '
        total_count = 0
        game = i + 1
        winning_numbers = [int(n) for n in t.split('|')[0].split(':')[1].split() if n.isdigit() ]
        your_numbers = [int(n) for n in t.split('|')[1].split() if n.isdigit()]
        your_numbers_counter = Counter(your_numbers)               
        for ii, w_n in enumerate(winning_numbers):
            total_count += your_numbers_counter[w_n]
            print ("game: ", game," ",ii + 1, "wn: ", w_n, "your numbers: ",your_numbers, "winning numbers: ", winning_numbers, "count :", your_numbers_counter[w_n])
        y_winnings = score(total_count)
        winnings += y_winnings
        print("game: ",game, "total_count ",total_count, "winnings : ", y_winnings, "total:", winnings)

    print(int(winnings))
    return winnings

def score(c):
    if c == 0:
        return 0
    if c == 1:
        return 1
    if c>1:
        return  2**(c-1)

def main():
    a = get_input()
    parse_tickets(a)
    print([(score(x), x) for x in range(10)])


main()
    


