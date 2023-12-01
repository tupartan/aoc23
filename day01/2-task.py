intMap = {
  "one"   : "1",
  "two"   : "2",
  "three" : "3",
  "four"  : "4",
  "five"  : "5",
  "six"   : "6",
  "seven" : "7",
  "eight" : "8",
  "nine"  : "9",
}

def findNumbers(s):
  output = {}
  
  for x in intMap:
    index = 0
    while s.find(x, index) != -1:
      pos = s.find(x, index)
      output[pos] = intMap[x]
      index = pos+1
  return output

f = open("2-input", "r")
sum = 0

for x in f:
  mapOfPos = findNumbers(x)
  s = ''.join(filter(str.isdigit, x))
  for number in s:
    index = 0
    while x.find(number, index) != -1:
      p = x.find(number, index)
      mapOfPos[p] = number
      index = p+1

  sorts = dict(sorted(mapOfPos.items()))
  add = int(list(sorts.values())[0] + list(sorts.values())[len(sorts)-1])
  sum += add

print(sum)