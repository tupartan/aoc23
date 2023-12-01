f = open("1-input", "r")
sum = 0
for x in f:
  s = ''.join(filter(str.isdigit, x))
  if(len(s) == 0):
    break
  else:
    sum += int(s[0]+s[-1])

print(sum)