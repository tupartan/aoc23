import re

def plot(source, range):
  ranges = range.split(" ")
  dstRngStart = int(ranges[0])
  srcRngStart = int(ranges[1])
  rangeLength = int(ranges[2])
  #print("Plotting {} between {} and {}".format(source, srcRngStart, srcRngStart + rangeLength))
  if(source < srcRngStart or source > srcRngStart + rangeLength): return False
  else: 
    #print("Match {}".format((source - srcRngStart) + dstRngStart))
    return (source - srcRngStart) + dstRngStart

with open("1-input", "r") as f:
  seeds = None
  map = None
  maps = {}
  for row in f:
    if(re.search("seeds", row)): seeds = row.split(":")[1].strip().split(" ")
    if(re.search("map", row)):
      map = row.split(":")[0].split(" ")[0]
    if(re.search("^(\d+ \d+ \d+)", row)):
      if(map not in maps): maps[map] = []
      maps[map].append(row.strip())

print("Seeds: {}".format(seeds))
print(maps)

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
    print("{} mapped with {} to {}".format(seed, map, result))

print("Location: {}".format(lowest))