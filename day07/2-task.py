from typing import Final
from operator import countOf
import numpy as np
import string

# Types of cards
A: Final[int] = 14
K: Final[int] = 13
Q: Final[int] = 12
T: Final[int] = 10
J: Final[int] = 1

# Types of hand
FIVE_OF_A_KIND:  Final[int] = 7
FOUR_OF_A_KIND:  Final[int] = 6
FULL_HOUSE:      Final[int] = 5
THREE_OF_A_KIND: Final[int] = 4
TWO_PAIRS:       Final[int] = 3
ONE_PAIR:        Final[int] = 2
HIGH_CARD:       Final[int] = 1

class Comparable:
  #Rich comparison methods
  def __lt__(self, other):
    return self._cmp(other) < 0
  def __le__(self, other):
    return self._cmp(other) <= 0
  def __eq__(self, other):
    return self._cmp(other) == 0
  def __ne__(self, other):
    return self._cmp(other) != 0
  def __ge__(self, other):
    return self._cmp(other) >= 0
  def __gt__(self, other):
    return self._cmp(other) > 0

class Hand(Comparable):

  def __init__(self, hand, bid):
    self.cards = []
    for char in hand:
      self.cards.append(Card(char))
    self.type = self.setType()
    self.bid = bid

  def __str__(self):
    handStr = ""
    for c in self.cards:
      handStr += str(c)
    return handStr
  
  def setType(self):
    counts = {}
    for x in range(2, 15):
      count = self.cards.count(Card(x))
      if(count > 0): counts[x] = count
    jokers = self.cards.count(Card(J))
    if(5 in counts.values() or (4 in counts.values() and jokers == 1) or (3 in counts.values() and jokers == 2) or (2 in counts.values() and jokers == 3) or (jokers >= 4)): return FIVE_OF_A_KIND
    if(4 in counts.values() or (3 in counts.values() and jokers == 1) or (2 in counts.values() and jokers == 2) or (jokers == 3)): return FOUR_OF_A_KIND
    if((3 in counts.values() and 2 in counts.values()) or (countOf(counts.values(), 2) == 2 and jokers == 1) ): return FULL_HOUSE
    if((3 in counts.values()) or (2 in counts.values() and jokers == 1) or (jokers == 2)): return THREE_OF_A_KIND
    if(countOf(counts.values(), 2) == 2): return TWO_PAIRS
    if((2 in counts.values()) or jokers == 1): return ONE_PAIR
    return HIGH_CARD

  def _cmp(self, other):
    if(self.type - other.type == 0):
      for x in range(5):
        if(self.cards[x] != other.cards[x]): return self.cards[x].card - other.cards[x].card
    return self.type - other.type

class Card(Comparable):
  def __init__(self, card):
    if(card == "A"): self.card = A
    elif(card == "K"): self.card = K
    elif(card == "Q"): self.card = Q
    elif(card == "J"): self.card = J
    elif(card == "T"): self.card = T
    else: self.card = int(card)
  def __str__(self):
    if(self.card == 14): return "A"
    elif(self.card == 13): return "K"
    elif(self.card == 12): return "Q"
    elif(self.card == 10): return "T"
    elif(self.card == 1): return "J"
    else: return str(self.card)
  def _cmp(self, other):
    return self.card - other.card 

with open("2-input", "r") as f:
  hands = np.array([])
  for row in f:
    hands = np.append(hands, Hand(row.split(" ")[0], int(row.split(" ")[1].strip())))
  
  winnings = 0
  rank = 1
  for hand in np.sort(hands):
    winnings += rank * hand.bid
    print(f'{hand.type} {hand} {hand.bid}')
    rank += 1

print(f'Total winnings {winnings}')