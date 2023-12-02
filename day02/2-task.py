import re

class Game:
  
  def __init__(self, id):
    self.id = int(id)
    self.minRed = 0
    self.minGreen = 0
    self.minBlue = 0

  def addSets(self, row):
    results = row.rstrip().split(":")[1].split(";")
    for result in results:
      r = re.findall("(\d+)\s(red|green|blue)", result)
      dices = {"red"   : 0, "green" : 0, "blue"  : 0}
      for(amount, color) in r:
        dices[color] = int(amount)
      if(dices["red"] > self.minRed): self.minRed = dices["red"]
      if(dices["green"] > self.minGreen): self.minGreen = dices["green"]
      if(dices["blue"] > self.minBlue): self.minBlue = dices["blue"]
 
  def getPower(self):
    return self.minRed * self.minGreen * self.minBlue

f = open("2-input", "r")

sum = 0
for row in f:
  game = Game(row.split(":")[0].split(" ")[1])
  game.addSets(row)
  sum = sum + game.getPower()

print(sum)