from typing import Final
from math import lcm
import re

class Map:
  def __init__(self, instructions, positions):

    self.L: Final[int] = 0
    self.R: Final[int] = 1
    
    self.instructions = instructions
    self.positions = positions
  
  def getInstruction(self, i):
    if(self.instructions[i] == "L"): return self.L
    else: return self.R

  def travelTo(self, start, end):
    steps = 0
    currentPosition = start
    while(not re.findall(end, currentPosition)):
      currentPosition = self.positions[currentPosition][self.getInstruction(steps % len(self.instructions))]
      steps += 1
    return steps

with open("2-input", "r") as f:
  instructions = list(f.readline().rstrip())
  mapEntries = filter(None, (row.rstrip() for row in f))
  positions = {}
  for entry in mapEntries:
    split = entry.split(" = ")
    positions[split[0]] = [split[1].split(", ")[0].replace("(", ""), split[1].split(", ")[1].replace(")", "")]
  map = Map(instructions, positions)
  
  s = re.compile("\w\wA")
  e = re.compile("\w\wZ")
  startingPoints = list(filter(s.match, map.positions))
  steps = []
  for x in range(len(startingPoints)):
    steps.append(map.travelTo(startingPoints[x], e))

  print(f'Total: {lcm(*steps)}')