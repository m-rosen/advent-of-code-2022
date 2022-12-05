
from sys import stdin

# Read stacks
line = stdin.readline()
nr_stacks = len(line) // 4
stacks = [[] for i in range(0, nr_stacks)]

while line[1] != '1':
  for i in range(0, nr_stacks):
    item = line[1 + i*4]
    if item != ' ':
      stacks[i].append(item)

  line = stdin.readline()

stdin.readline() # Discard blank line

# Process moves
for line in stdin:
  _, moves, _, src, _ , dst = line.strip().split()

  for i in range(0, int(moves)):
    item = stacks[int(src) - 1].pop(0)
    stacks[int(dst) - 1].insert(0, item)

res = ""
for s in stacks:
  res += s[0]

print(res)