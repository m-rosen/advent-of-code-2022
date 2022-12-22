from sys import argv
import operator
import time

OP = { '-': operator.sub, '+': operator.add, '/': operator.truediv, '*': operator.mul }
ANTI_OP = { '+': operator.sub, '-': operator.add, '*': operator.truediv, '/': operator.mul}

def read_input(f):
  monkeys = {}
  for line in f:
    tokens = line.strip().split()
    if len(tokens) == 4:
      name, left, op, right = tokens
      monkeys[name.strip(':')] = (left, op, right) 
    else:
      name, value = tokens
      monkeys[name.strip(':')] = (value, ) 
  return monkeys


def eval(name, monkeys):
  expr = monkeys[name]
  if len(expr) == 1:
    return int(expr[0])
  else:
    left, op, right = expr
    return OP[op](eval(left, monkeys), eval(right, monkeys))


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  
  monkeys = read_input(open(argv[1]))
  print(eval('root', monkeys))
  
  print(round(time.time() - start_t, 3), 's')


def eval_2(name, monkeys):
  expr = monkeys[name]
  if len(expr) == 1:
    if expr[0] == '?':
      return ('?',)
    else:
      return int(expr[0])
  else:
    left, op, right = expr
    l_val = eval_2(left, monkeys)
    r_val = eval_2(right, monkeys)
    if type(l_val) == tuple or type(r_val) == tuple:
      return (l_val, op, r_val)
    return OP[op](l_val, r_val)


def solve(val, expr):
  l, op, r = expr

  if l == ('?',):
    return ANTI_OP[op](val, r)
  elif r == ('?',):
    if op == '-' or op == '/':
      return OP[op](l, val)
    else:
      return ANTI_OP[op](val,l)

  if type(l) != tuple:
    if op == '-' or op == '/':
      val = OP[op](l, val)
    else:
      val = ANTI_OP[op](val, l)
    return solve(val, r)
      
  elif type(r) != tuple:
    val = ANTI_OP[op](val, r)
    return solve(val, l)


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  
  monkeys = read_input(open(argv[1]))
  monkeys['humn'] = '?'

  left, _, right = monkeys['root']
  l_val = eval_2(left, monkeys)
  r_val = eval_2(right, monkeys)

  print(solve(r_val, l_val))

  print(round(time.time() - start_t, 3), 's')
