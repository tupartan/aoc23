class Race:
  def __init__(self, record, distance):
    self.record = record
    self.distance = distance
  
  def beatRecord(self, speed):
    holds = 0
    for hold in range(1, self.record):
      if(speed * hold * (self.record - hold) > self.distance):
        holds += 1
    return holds

with open("2-input", "r") as f:
  records = [f.readline().split(":")[1].replace(" ", "").strip()]
  distances = [f.readline().split(":")[1].replace(" ", "").strip()]
  races = []
  for i in range(len(records)):
    races.append(Race(int(records[i]), int(distances[i])))
  
  sums = []
  for race in races:
    sums.append(race.beatRecord(1))
  total = 0
  for sum in sums:
    if(total == 0): total = sum
    else: total *= sum
  
  print(f'Total: {total}')