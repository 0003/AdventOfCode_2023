'''--- Day 7: Camel Cards ---'''
#works
import functools
import operator
import collections

labels = ["A", 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2','J'] #reorder J
ranks = list(range(len(labels),0,-1))
labels_rank = dict(zip(labels,ranks))

class Hand:
    def __init__(self,hand,bid):
        self.bid = bid
        self.hand = hand
        self.counts = collections.Counter(hand)
        self.counter_test = self.counts.values()
        self.hand_strength = self.calc_joker_hand_strenghth()
        self.single_cards_strengths = [labels_rank[c] for c in hand ] #5 ranks 13 to 1
        self.joker_hand = self.hand #initial

    def calc_joker_hand_strenghth(self):
        j_count = self.counts['J']
        #print(f"j count: {j_count}, self.counts= {self.counts}")
        if j_count == 5:
            return 7
        elif 1 <= j_count <= 4:
            temp_counts_not_joker = collections.defaultdict(int)
            for c in self.hand:
                if c != 'J':
                    temp_counts_not_joker[c] += 1
            top_card = sorted(temp_counts_not_joker.items(),key=lambda x: x[1], reverse=True)[0][0] #first element, and then card
            self.joker_hand = ''.join([top_card if c == 'J' else c for c in self.hand ]) 
            #print(f" {self.hand}---->{self.joker_hand}-----------Joker found ---------top card: {top_card}")
            return self.calc_hand_strengh(J=True)                       
        else:
            return self.calc_hand_strengh()
        

    def calc_hand_strengh(self,J=False):
        if J == True:
            og_counts = self.counter_test
            temp_counts = collections.Counter(self.joker_hand).values()
            self.counter_test = temp_counts #we replace this back on exit
        strength = 1
        #test for five of a kind:
        if 5 in self.counter_test:
            strength = 7
        #test for four of a kind
        elif 4 in self.counter_test:
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

        if J==True:
            self.counter_test = og_counts
        return strength

def ranker(hand1,hand2):
    if not isinstance(hand1,Hand) and not isinstance(hand2,Hand):
        raise TypeError(f"wrong inputs {hand1} and {hand2}") 

    if hand1.hand_strength > hand2.hand_strength:
        return 1
    elif hand1.hand_strength < hand2.hand_strength:
        return -1
    else:
        for i in range(5):
            if hand1.single_cards_strengths[i] > hand2.single_cards_strengths[i]:
                return 1
            elif hand1.single_cards_strengths[i] < hand2.single_cards_strengths[i]:
                return -1
    return 0

def get_input(fi):
    with open(fi) as f:
        ingest = [i.split() for i in f.readlines()]
        cards_bids = [(hand, int(bid)) for hand, bid in ingest]
        print(cards_bids[:5])
        return cards_bids

def main(fi):
    print(f'label ranks:\n{labels_rank}')
    cards_bids = get_input(fi)

    length = len(cards_bids)
    bids_sorted = sorted([cb[1] for cb in cards_bids ])
    a = sum(x*y for x,y in zip(bids_sorted,range(length,1,-1)))
    b = sum(x*y for x,y in (zip(bids_sorted,range(1,length,1))))
    min_output, max_output = min(a,b), max(a,b)
    print(f"min output: {min_output}, max output: {max_output} range = {max_output - min_output}")

    cl_hands_bids = [Hand(cb[0],cb[1]) for cb in cards_bids]
    #print(cl_hands_bids)
    cl_hands_bids = sorted(cl_hands_bids,key=lambda hand: (hand.hand_strength, hand.single_cards_strengths),reverse=True)

    rank = length #5 in test case
    i = 0
    winnings = 0
    for card_hand in cl_hands_bids:
        print(card_hand.hand, card_hand.bid, f'rank: {rank - i}',
               f'hand strength: {card_hand.hand_strength}', 
               f'cards strength: {card_hand.single_cards_strengths}',
                f'counts: {card_hand.counts} ' )
        winnings += card_hand.bid * (rank - i)
        i += 1
        print(f'cumulative winnings: {winnings}')
    print(f'winnings= {winnings}')
    print(f"min output: {min_output}, max output: {max_output} range = {max_output - min_output}, test: {min_output<=winnings<=max_output}")
    return winnings

#main('7/test.txt')
#main('7/test_mine.txt')
main('7/input.txt')