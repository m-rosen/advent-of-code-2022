from sys import stdin
from math import lcm
import operator

ops = { '+': operator.add, '*': operator.mul }

items = []
test = []
operation = []
value = []
dest = []
nr_monkeys = 0

# Read input
while stdin.readline():
  its = stdin.readline().strip().split(":")[-1]
  its = [int(it) for it in its.split(",")]
  _, _, _, _, op, val = stdin.readline().strip().split()
  val = int(val) if val != "old" else "old"
  t = stdin.readline().strip().split()[-1]
  t = int(t)
  true_dest = stdin.readline().strip().split()[-1]
  false_dest = stdin.readline().strip().split()[-1]

  items.append(its)
  test.append(t)
  operation.append(ops[op])
  value.append(val)
  dest.append((int(true_dest), int(false_dest)))
  stdin.readline() # Discard blank row
  nr_monkeys += 1

'''------------------------------------------------'''

# nr_rounds = 20 # For part 1
nr_rounds = 10000 # For part 2

activity = [ 0 for _ in range (0, nr_monkeys)]
lcm_test = lcm(*test)

def throw(src, dest, new_val):
  if len(items[src]) > 0:
    items[dest].append(new_val)
    del items[src][0]

# Monkey business
for _ in range(0, nr_rounds):
  for monkey in range(0, nr_monkeys):
    if len(items[monkey]) == 0:
      continue
  
    while len(items[monkey]) > 0:
      worry = items[monkey][0]
      if value[monkey] == "old":
        worry = operation[monkey](worry, worry)
      else:
        worry = operation[monkey](worry, value[monkey])

      # worry = worry // 3 # For part 1
      worry = worry % lcm_test

      if worry % test[monkey] == 0:
        throw(monkey, dest[monkey][0], worry)
      else:
        throw(monkey, dest[monkey][1], worry)

      activity[monkey] += 1

activity.sort(reverse=True)

result = activity[0] * activity[1]
print(result)