f = open("2-input", "r")

class Card:
  def __init__(self, id, checkNumbers, playNumbers):
    self.id = id
    self.checkNumbers = self.sortList(checkNumbers)
    self.playNumbers = self.sortList(playNumbers)
    self.matches = self.countMatches()
  
  def countMatches(self):
    matches = 0
    for checkNumber in self.checkNumbers:
      for playNumber in self.playNumbers:
        if(checkNumber == playNumber):
          matches += 1
          break
        elif(checkNumber < playNumber): break
    return matches

  def sortList(self, list):
    unSorted = []
    for number in list:
      unSorted.append(int(number))
    return sorted(unSorted)
  
class Deck:
  def __init__(self, file):
    self.nocs = {}
    self.cards = []
    for row in file:
      id = int(list(filter(None, row.split(":")[0].split(" ")))[1])
      checkNumbers = list(filter(None, row.split(":")[1].split("|")[0].strip().split(" ")))
      playNumbers = list(filter(None, row.split(":")[1].split("|")[1].strip().split(" ")))
      self.cards.append(Card(id, checkNumbers, playNumbers))
      self.nocs[id] = 1
  
  def appendCard(self, id):
    self.nocs[id] += 1
  
  def countCards(self):
    count = 0
    for id in self.nocs:
      count += self.nocs[id]
    return count

  def processCards(self):
    for card in self.cards:
      i = 0
      while i < self.nocs[card.id]:      
        if(card.matches == 0): break
        for id in range(card.id + 1, card.id + 1 + card.matches):
          self.appendCard(id)
        i += 1

deck = Deck(f)
#print(deck.countCards())
deck.processCards()
print(deck.countCards())