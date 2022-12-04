
from sys import stdin

def getline_int():
  s = stdin.readline().strip()
  s = s if s else 0
  return int(s)

largest = [0,0,0]
current = 0

cal = getline_int()
while cal > 0:

  current = cal
  
  cal = getline_int()
  while cal > 0:
    current += cal
    cal = getline_int()
  
  if current > min(largest):
    largest.remove(min(largest))
    largest.append(current)

  cal = getline_int()

print("Three larges ration are: ", largest)
print("The total is: ", sum(largest))