'''--- Day 4: Scratchcards ---'''

#works_

import re
from collections import Counter

def get_input():
    with open('4/input.txt') as f:
        a = f.readlines()
        return a

def score(c):
    if c == 0:
        return 0
    if c == 1:
        return 1
    if c>1:
        return  2**(c-1)

def parse_tickets(a,bag_of_cards):
    winnings = 0
    for i,t in enumerate(a):
        t += ' '
        total_count = 0
        game = i + 1

        #dont change
        winning_numbers = [int(n) for n in t.split('|')[0].split(':')[1].split() if n.isdigit() ]
        your_numbers = [int(n) for n in t.split('|')[1].split() if n.isdigit()]
        your_numbers_counter = Counter(your_numbers)

        for ii, w_n in enumerate(winning_numbers):
            total_count += your_numbers_counter[w_n]
        
        #add this 
        game_winnings = score(total_count) * ( bag_of_cards[game] + 1 )
        winnings += game_winnings
        #more cards
        if total_count > 0:
            r_ = range(game +1 , game + total_count + 1) 
            print("game: ", game, "won ", total_count, " tickets so adding", r_)
            for iii in r_:
                bag_of_cards[iii] += 1 * bag_of_cards[game]
        else:
            print("game: ", game, "loss ", total_count, " no tickets so adding")
        
        print("after game: ",game, "winnings : ", game_winnings,
               "total:", winnings,"bag of cards:", sum(bag_of_cards.values()),"\n",sorted(bag_of_cards.items(),key=lambda x: x[0]))


    print("winnings: ", int(winnings))
    print("total bag of cards: ", sum(bag_of_cards.values()))
    return winnings

def main():
    a = get_input()
    bag_of_cards = Counter()
    for i in range(len(a)):
        bag_of_cards[i+1] += 1
    print("Initial :", sum(bag_of_cards.values()), " ", sorted(bag_of_cards.items(),key=lambda x: x[0]))
    parse_tickets(a,bag_of_cards)
    print(sorted(bag_of_cards.items(),key=lambda x: x[0]))
    print(sum(bag_of_cards.values()))
          
main()
    


