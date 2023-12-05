import re

def plot(source, range):
  ranges = range.split(" ")
  dstRngStart = int(ranges[0])
  srcRngStart = int(ranges[1])
  rangeLength = int(ranges[2])
  if(source < srcRngStart or source > srcRngStart + rangeLength): return False
  else: 
    return (source - srcRngStart) + dstRngStart

with open("2-input", "r") as f:
  seeds = []
  map = None
  maps = {}
  for row in f:
    if(re.search("seeds", row)): 
      allSeeds = row.split(":")[1].strip().split(" ")
      for x in range(0, len(allSeeds), 2):
        for y in range(int(allSeeds[x]), int(allSeeds[x]) + int(allSeeds[x+1])):
          seeds.append(y)
    if(re.search("map", row)):
      map = row.split(":")[0].split(" ")[0]
    if(re.search("^(\d+ \d+ \d+)", row)):
      if(map not in maps): maps[map] = []
      maps[map].append(row.strip())

#print("Seeds: {}".format(seeds))
#print(maps)

lowest = 0
for seed in seeds:
  nextSeed = int(seed)
  for map in maps:
    for parameters in maps[map]:
      result = plot(nextSeed, parameters)
      if(result): break
    if(not result): result = nextSeed
    nextSeed = result
    if(map == "humidity-to-location"):
      if(lowest == 0): lowest = result
      if(result < lowest): lowest = result
    #print("{} mapped with {} to {}".format(seed, map, result))

print("Location: {}".format(lowest))