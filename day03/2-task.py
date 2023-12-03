import re

file = open("2-input", "r")
# 540131 86879020

def findIfAdjacent(digit, x, y):
  digitLength = len(digit)
  for xPos in range(x-1, x + 2):
    for yPos in range(y-1, y + digitLength + 1):
      if xPos in symbols.keys():
        if yPos in symbols[xPos].keys():
          if(symbols[xPos][yPos] == 0): symbols[xPos][yPos] = -1 * int(digit)
          elif(symbols[xPos][yPos] < 0): symbols[xPos][yPos] *= -1 * int(digit)
          return True
  return False

x = 0
symbols = {}
for row in file:
  y = 0
  for character in row.rstrip():
    if(character == "*"):
      if x in symbols.keys():
        symbols[x][y] = 0
      else: symbols[x] = {y:0}
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

gears = 0
for row in symbols:
  for item in symbols[row]:
    if(symbols[row][item] > 0): gears += symbols[row][item]

print(gears)