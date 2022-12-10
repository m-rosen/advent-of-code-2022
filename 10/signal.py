
from sys import stdin 

x = 1
cycle = 0
sum = 0

for line in stdin:
  line = line.strip()

  cycle += 1
  if cycle >= 20 and (cycle - 20) % 40 == 0:
    sum += cycle * x

  
  instr = line[0:4]
  if instr == "addx":
    cycle += 1
    if cycle >= 20 and (cycle - 20) % 40 == 0:
      sum += cycle * x

    _ , v = line.split()
    x += int(v)

print(sum)
   