import collections

# namedtuple: used to create a class of objects that are just attributes with no custom method
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

card = Card('7', 'hearts')
print('card: ', card)
deck = FrenchDeck()
print('deck[0]: ', deck[0])

# Implementing special methods (__*__) allow to benefits from Python standard library, avoid confusion
from random import choice
print('choice(deck): ', choice(deck))

# __getitem__ delegates to the [] operator -> support slicing:
print('deck[9:13]: ', deck[9:13])
print('deck[12::13]: ', deck[12::13]) # Start::Step, take everything with a specific step

# By implementing __getitem__ -> iterable
for card in deck:
    print(card)

# Iteration is implicit, the deck doesn't implement __contains__, then uses sequential scan with __getitem__
print(Card('Q', 'hearts') in deck)
print(Card('12', 'hearts') in deck)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)
