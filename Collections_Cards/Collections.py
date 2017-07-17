# -*- coding: utf-8 -*-


import collections

import random

from collections import OrderedDict

Card = collections.namedtuple('Card',['rank', 'suit'])

class FrenchDesk():

    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split(' ')

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks
                                        for suit in self.suits]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

suit_values=dict(spades=3, diamonds=2, clubs=1, hearts=0)
print suit_values

def com_values(card):
    rank_value = FrenchDesk.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

desk = FrenchDesk()

for card in sorted(desk, key=com_values):
    print card



beer_card = Card('7','diamonds')

print beer_card



print len(desk)

#for card in desk:
#    print card

for x in range(1, 11):
    print random.choice(desk)

items = (('A', 1), ('B', 2), ('C', 3))
rDict = dict(items)
oDict = OrderedDict(items)

print rDict
for k, v in oDict.items():
    print k, v


