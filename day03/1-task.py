import re

file = open("1-input", "r")
# 540131 86879020

def findIfAdjacent(digit, x, y):
  digitLength = len(digit)
  for xPos in range(x-1, x + 2):
    for yPos in range(y-1, y + digitLength + 1):
      print("check {} in ({}, {}) with {} {}".format(digit, x, y, xPos, yPos))
      if xPos in symbols.keys():
        if yPos in symbols[xPos].keys():
          #print("hit {} in ({}, {}) with {} {}".format(digit, x, y, xPos, yPos))
          return True
  return False

x = 0
symbols = {}
for row in file:
  y = 0
  for character in row.rstrip():
    if(character != "."):
      if(not character.isdigit()):
        if x in symbols.keys():
          symbols[x][y] = character
        else: symbols[x] = {y:character}
    y += 1
  x += 1
#print(symbols)
integers = 0
file.seek(0)

x = 0
for row in file:
  partNumbers = re.findall("(\d+)", row)
  i = 0
  for number in partNumbers:
    pos = row.find(number, i)
    #print("checking {} in ({}, {}, +{})".format(number, pos, i, len(number)))
    if(pos == -1): break
    if(findIfAdjacent(number, x, pos)):
      integers += int(number)
    i = pos + len(number) + 1
  x += 1

print(integers)