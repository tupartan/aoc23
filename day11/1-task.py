import numpy as np

class Galaxy:
  def __init__(self, position):
    self.position = position
  def distance(self, other):
    return abs(self.position[0] - other.position[0]) + abs(self.position[1] - other.position[1])

class Universe:
  def __init__(self, file):
    self.starMap = []
    self.galaxies = []
    for row in file:
      self.starMap.append(list(row.strip()))
    self.expand()
    self.map()
    
  def __str__(self):
    starMap = ""
    for row in self.starMap:
      starMap += "".join(row) + "\n"
    return starMap
  
  def expand(self):

    # Find empty verticals
    eV = []
    for v in range(len(self.starMap)):
      e = True
      for c in self.starMap[v]:
        if(c != "."):
          e = False
          break
      if(e):
        eV.append(v)
    
    # Find empty horizontals
    hV = []
    for h in range(len(self.starMap[0])):
      e = True
      for v in range(len(self.starMap)):
          if(self.starMap[v][h] != "."):
            e = False
            break
      if(e):
        hV.append(h)

    # Expansion
    i = 0
    for v in eV:
      self.starMap.insert(v+i, ["." * len(self.starMap[0])])
      i += 1
    for r in range(len(self.starMap)):
      j = 0
      for h in hV:
        self.starMap[r].insert(h+j, ".")
        j += 1

  def map(self):
    self.galaxies = []
    for r in range(len(self.starMap)):
      for c in range(len(self.starMap[r])):
        if(self.starMap[r][c] == "#"):
          self.galaxies.append(Galaxy([r, c]))

with open("1-input", "r") as f:
  u = Universe(f)
  sum = 0

  y = 1
  for galaxy in u.galaxies:
    for j in range(y, len(u.galaxies)):
      sum += galaxy.distance(u.galaxies[j])
    y += 1

print(sum)