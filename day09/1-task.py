class Report:
  def __init__(self, numbers):
    self.numbers = numbers
    self.extrapolatedValue = self.analyze()
  def analyze(self):
    i = 0
    differences = {}
    differences[i] = self.numbers
    while(not self.checkIfZero(differences[i])):
      i += 1
      differences[i] = []
      for n in range(1, len(differences[i-1])):
        differences[i].append(differences[i-1][n] - differences[i-1][n-1])
    differences[i].append(0)
    while(i > 0):
      i -= 1
      differences[i].append(differences[i][-1] + differences[i+1][-1])
    return differences[0][-1]
  
  def checkIfZero(self, numbers):
    for number in numbers:
      if(number != 0): return False
    return True

with open("1-input", "r") as f:
  reports = []
  for row in f:
    numbers = []
    split = row.split(" ")
    for number in split:
      numbers.append(int(number))
    report = Report(numbers)
    reports.append(report)

sums = 0
for report in reports:
  sums += report.extrapolatedValue

print(f'Total: {sums}')
#1934898178 1129