
f = open("1-input", "r")

def sortList(list):
  unSorted = []
  for number in list:
    unSorted.append(int(number))
  return sorted(unSorted)

sum = 0
for row in f:
  gameId = row.split(":")[0].split(" ")[1]
  checkNumbers = sortList(list(filter(None, row.split(":")[1].split("|")[0].strip().split(" "))))
  playNumbers = sortList(list(filter(None, row.split(":")[1].split("|")[1].strip().split(" "))))
  print("Game {} check: {} with {}".format(gameId, checkNumbers, playNumbers))

  gamePoints = 0
  for checkNumber in checkNumbers:
    print("checkNumber {}".format(checkNumber))
    for playNumber in playNumbers:
      print("playNumber {}".format(playNumber))
      if(checkNumber == playNumber):
        if(gamePoints == 0): gamePoints += 1
        else: gamePoints *= 2
        print("match! game points {}".format(gamePoints))
        break
      elif(checkNumber < playNumber): break
  print("Gamepoints {}".format(gamePoints))
  sum += gamePoints

print(sum)