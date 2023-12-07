import functools
import operator
import collections

labels = ["A", 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
ranks = list(range(len(labels),0,-1))
labels_rank = dict(zip(labels,ranks))

class Hand:
    def __init__(self,hand,bid):
        self.bid = bid
        self.hand = hand
        self.counter_test = collections.Counter(hand).values()
        self.hand_strength = self.calc_hand_strengh()
        self.single_cards_strengths = [labels_rank[c] for c in hand ] #5 ranks 13 to 1
        
    def calc_hand_strengh(self):
        strength = 0
        #test for five of a kind:
        if 5 in self.counter_test:
            strength = 7
        #test for four of a kind
        elif 4 in self.counter_test == 4:
            strength = 6
        #test for full house
        elif 3 in self.counter_test and 2 in self.counter_test:
            strength = 5
        #three pair test
        elif 3 in self.counter_test and 2 not in self.counter_test:
            strength= 4
        #two pairs
        elif functools.reduce(operator.mul,self.counter_test) == 4 and 2 in self.counter_test:
            strength = 3
        elif functools.reduce(operator.mul,self.counter_test) == 2:
            strength = 2
        else:
            strength = 1
        return strength

def ranker(hand1,hand2):
    if not isinstance(hand1,Hand) and not isinstance(hand2,Hand):
        raise TypeError(f"wrong inputs {hand1} and {hand2}") 

    if hand1.hand_strength > hand2.hand_strength:
        return hand1
    elif hand1.hand_strength < hand2.hand_strength:
        return hand2
    else:
        for i in range(5):
            if hand1.hand_strength[i] > hand2.hand_strength[i]:
                return hand1
            elif hand1.hand_strength[i] < hand2.hand_strength[i]:
                return hand2
    return hand1

def get_input():
    with open('7/input.txt') as f:
        ingest = [i.split() for i in f.readlines()]
        cards_bids = [(hand, int(bid)) for hand, bid in ingest]
        print(cards_bids[:5])
        return cards_bids

def main():
    print(f'label ranks:\n{labels_rank}')
    cards_bids = get_input()
    length = len(cards_bids)
    bids_sorted = sorted([cb[1] for cb in cards_bids ])
    a = sum(x*y for x,y in zip(bids_sorted,range(length,1,-1)))
    b = sum(x*y for x,y in (zip(bids_sorted,range(1,length,1))))
    min_output, max_output = min(a,b), max(a,b)
    print(f"min output: {min_output}, max output: {max_output} range = {max_output - min_output}")

    cl_hands_bids = [Hand(cb[0],cb[1]) for cb in cards_bids]
    #print(cl_hands_bids)
    cl_hands_bids = sorted(cl_hands_bids,key=lambda hand1,hand2: ranker(hand1,hand2))

    rank = length
    i = 0
    winnings = 0
    for card in cl_hands_bids:
        print(card.hand, card.bid, rank - i )
        winnings += card.bid * rank - i
        i -= 1
    print(f'winnings={winnings}')
    return winnings

main()