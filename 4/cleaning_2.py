from sys import stdin

overlaps = 0

for line in stdin:
  a, b = line.strip().split(',')

  a = [int(i) for i in a.split('-')]
  b = [int(i) for i in b.split('-')]

  # a overlaps from left
  if a[0] <= b[0] and a[1] >= b[0]:
    overlaps += 1

  # b overlaps from left
  elif b[0] <= a[0] and b[1] >= a[0]:
    overlaps += 1

print("Number of overlaps:", overlaps)