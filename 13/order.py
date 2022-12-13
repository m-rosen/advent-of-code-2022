
from sys import stdin, argv
from functools import cmp_to_key
import json

'''
  Returns positive if in order, 0 is egual, and negative otherwise
'''
def in_order(a, b):
  if type(a) == int and type(b) == int: # both integers
    return b - a
  
  elif type(a) == list and type(b) == list: # both lists
    i = 0
    while i < min(len(a), len(b)):
      if (order := in_order(a[i], b[i])) != 0:
        return order
      i += 1
    return len(b) - len(a)

  elif type(a) == list:
    return in_order(a, [b]) # a is list b is integer
  else:
    return in_order([a], b) # b is list a is integer


if __name__ == '__main__' and len(argv) == 1:
  pair_idx = 1
  sum = 0

  while first := stdin.readline():
    first = json.loads(first.strip())
    second = json.loads(stdin.readline().strip())
    
    if in_order(first, second) > 0:
      sum += pair_idx

    stdin.readline() # Discard empty line
    pair_idx += 1

  print("Sum idx of in order pairs", sum)


if __name__ == '__main__' and len(argv) == 2 and argv[1] == '2':
  packet = [[[2]], [[6]]] # Dividers

  for line in stdin:
    line = line.strip()
    if line:
      p = json.loads(line)
      packet.append(p)
  
  packet.sort(key=cmp_to_key(in_order), reverse=True)
  
  print("Decoder key:", (packet.index([[2]]) + 1) * (packet.index([[6]]) + 1))