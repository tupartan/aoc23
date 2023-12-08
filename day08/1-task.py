from typing import Final

class Map:
  def __init__(self, instructions, positions):

    self.L: Final[int] = 0
    self.R: Final[int] = 1
    
    self.instructions = instructions
    self.positions = positions
    self.currentPosition = None
  
  def getInstruction(self, i):
    if(self.instructions[i] == "L"): return self.L
    else: return self.R

  def travelTo(self, start, end):
    steps = 0
    self.currentPosition = start
    while(self.currentPosition != end):
      self.currentPosition = self.positions[self.currentPosition][self.getInstruction(steps % len(self.instructions))]
      steps += 1
    return steps

with open("1-input", "r") as f:
  instructions = list(f.readline().rstrip())
  mapEntries = filter(None, (row.rstrip() for row in f))
  positions = {}
  for entry in mapEntries:
    split = entry.split(" = ")
    positions[split[0]] = [split[1].split(", ")[0].replace("(", ""), split[1].split(", ")[1].replace(")", "")]
  map = Map(instructions, positions)
  print(f'Total: {map.travelTo("AAA", "ZZZ")}')