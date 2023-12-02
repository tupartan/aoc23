import re

diceMap = {
  "red"   : 12,
  "green" : 13,
  "blue"  : 14
}

def getGameId(row):
  id = row.split(":")[0].split(" ")[1]
  return int(id)

def getGameResult(row):
  success = 0
  results = row.rstrip().split(":")[1].split(";")
  for result in results:
    r = re.findall("(\d+)\s(red|green|blue)", result)
    dices = {"red"   : 0, "green" : 0, "blue"  : 0}
    for(amount, color) in r:
      dices[color] = int(amount)
    if(possibleToPlay(dices["red"], dices["green"], dices["blue"])): success = success + 1
    else: return 0
  return success

def possibleToPlay(red, green, blue):
  if(red <= diceMap["red"] and green <= diceMap["green"] and blue <= diceMap["blue"]):
    return True
  else:
    return False

f = open("1-input", "r")

sum = 0
for x in f:
  if(getGameResult(x) > 0): sum = sum + getGameId(x)
print(sum)