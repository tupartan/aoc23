from typing import Final

START:      Final[str] = "S"
VERTICAL:   Final[str] = "|"
HORIZONTAL: Final[str] = "-"
NORTH_EAST: Final[str] = "L"
NORTH_WEST: Final[str] = "J"
SOUTH_WEST: Final[str] = "7"
SOUTH_EAST: Final[str] = "F"

class Map:
  def __init__(self, map):
    self.map = map
  def north(self, position):
    try:
      tile = self.map[position[0]][position[1]]
      north = None
      if(tile == START or tile == VERTICAL or tile == NORTH_WEST or tile == NORTH_EAST):
        north = [position[0]-1, position[1]]
        northTile = self.map[position[0]-1][position[1]]
        if(not(northTile == VERTICAL or northTile == SOUTH_EAST or northTile == SOUTH_WEST)):
          north = False
    except: north = False
    return north
  def east(self, position):
    try:
      tile = self.map[position[0]][position[1]]
      east = None
      if(tile == START or tile == HORIZONTAL or tile == NORTH_EAST or tile == SOUTH_EAST):
        east = [position[0], position[1]+1]
        eastTile = self.map[position[0]][position[1]+1]
        if(not(eastTile == HORIZONTAL or eastTile == NORTH_WEST or eastTile == SOUTH_WEST)):
          east = False
    except: east = False
    return east
  def south(self, position):
    try:
      tile = self.map[position[0]][position[1]]
      south = None
      if(tile == START or tile == VERTICAL or tile == SOUTH_EAST or tile == SOUTH_WEST):
        south = [position[0]+1, position[1]]
        southTile = self.map[position[0]+1][position[1]]
        if(not(southTile == VERTICAL or southTile == NORTH_WEST or southTile == NORTH_EAST)):
          south = False
    except: south = False
    return south
  def west(self, position):
    try:
      tile = self.map[position[0]][position[1]]
      west = None
      if(tile == START or tile == HORIZONTAL or tile == NORTH_WEST or tile == SOUTH_WEST):
        west = [position[0],position[1]-1]
        westTile = self.map[position[0]][position[1]-1]
        if(not(westTile == HORIZONTAL or westTile == NORTH_EAST or westTile == SOUTH_EAST)):
          west = False
    except: west = False
    return west
  def findRoutes(self, position):
    routes = []
    if(self.north(position)): routes.append(self.north(position))
    if(self.east(position)): routes.append(self.east(position))
    if(self.south(position)): routes.append(self.south(position))
    if(self.west(position)): routes.append(self.west(position))
    return routes
  def checkPositions(self, positions):
    position = positions[0]
    for x in range(1, len(positions)):
      if(not position == positions[x]):
        return False
    return True
  
class Route:
  def __init__(self, start, position, map):
    self.prevPosition = start
    self.position = position
    self.steps = 1
    self.map = map
  def __eq__(self, other):
    return self.position == other.position
  def takeStep(self):
    routes = self.map.findRoutes(self.position)
    if(len(routes) == 0): print(f'No route in {self.position}')
    for route in routes:
      if(route != self.prevPosition):
        self.prevPosition = self.position
        self.position = route
        self.steps += 1
        return
  
with open("1-input", "r") as f:
  map = []
  x = -1
  y = -1
  for row in f:
    map.append(list(row.strip()))
    test = row.find("S")
    if(test != -1):
      x = test
      y = len(map)-1

m = Map(map)
start = [y,x]
firstSteps = m.findRoutes(start)
print(f'First: {firstSteps}')
routes = []
for step in firstSteps:
  routes.append(Route(start, step, m))

while not m.checkPositions(routes):
  for route in routes:
    route.takeStep()
    #if(m.checkPositions(routes)): break
    print(f'{route.steps} {route.position}')
  #if(route.steps > 10): break

for route in routes:
  print(f'Total steps: {route.steps}')