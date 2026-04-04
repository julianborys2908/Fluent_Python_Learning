import collections
import random

Card = collections.namedtuple('Card', ['rank', 'suit'])

# Example of representation of namedtuple defined above
beer_card = Card('7', 'diamonds')
print(f'Beer card: {beer_card}')


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    # .split() defaults to whitespaces
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, key):
        return self._cards[key]


deck = FrenchDeck()

# Usage of special method '__len__'
print(f'Length of the deck: {len(deck)} cards')

# Usage of special method '__getitem__'
print(f'Card examples: {deck[0]}, {deck[-1]}')

print(f'Card choosen randomly: {random.choice(deck)}')

print(f'Deck slicing: \n\t {deck[:3]}, \n\t {deck[12::13]}')

for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)  # ! Important line
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
