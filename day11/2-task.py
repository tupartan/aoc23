import numpy as np

class Galaxy:
  def __init__(self, position):
    self.position = position
    self.newPosition = None
  def addDistance(self, y, x):
    if(self.newPosition == None):
      self.newPosition = [self.position[0] + y, self.position[1] + x]
    else:
      self.newPosition = [self.newPosition[0] + y, self.newPosition[1] + x]
  def flush(self):
    if(self.newPosition != None):
      self.position = self.newPosition
      self.newPosition = None
  def distance(self, other):
    return abs(self.position[0] - other.position[0]) + abs(self.position[1] - other.position[1])

class Universe:
  def __init__(self, file):
    self.galaxies = []
    self.starMap = []
    y = 0
    for row in file:
      x = 0
      self.starMap.append(list(row.strip()))
      for c in row:
        if(c == "#"): self.galaxies.append(Galaxy([y, x]))
        x += 1
      y += 1
  def expand(self, factor):
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
    print(f'Verticals {eV} and Horizontal {hV}')
    for v in eV:
      for g in self.galaxies:
        if(g.position[0] > v):
          g.addDistance(factor, 0)
    for h in hV:
      for g in self.galaxies:
        if(g.position[1] > h):
          g.addDistance(0, factor)

with open("2-input", "r") as f:
  u = Universe(f)

u.expand(999999)
for g in u.galaxies:
  g.flush()
#  print(g.position)

sum = 0
y = 1
for galaxy in u.galaxies:
  for j in range(y, len(u.galaxies)):
    sum += galaxy.distance(u.galaxies[j])
  y += 1
print(f'Sum: {sum}')