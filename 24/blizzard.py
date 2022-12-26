from sys import argv
import time

def read_input(f):
  blizzards = set() # ((x,y), dir)
  w = h = 1
  start = end = None
  for j, line in enumerate(f):
    if j == 0:
      w = len(line) - 2 - 1 # -1 for \n
      start = (line.index('.') - 1, - 1)
      continue
    
    y = j - 1
    for i, c in enumerate(line):
      x = i - 1
      if c == '>':
        blizzards.add(((x, y), (1, 0)))
      elif c == '<':
        blizzards.add(((x, y), (-1, 0)))
      elif c == '^':
        blizzards.add(((x, y), (0, -1)))
      elif c == 'v':
        blizzards.add(((x, y), (0, 1)))
  
  h = y
  end = (line.index('.') - 1, y)
  
  return blizzards, start, end, w, h


def print_blizz(blizz, width, height):
  print('#' * (width + 2))
  b = [v[0] for v in blizz]
  for y in range(0, height):
    line = '#'
    for x in range(0, width):
      if (x, y) in b:
        line += 'B'
      else:
        line += ' '
    print(line + '#')
  print('#' * (width + 2))


def add_cord(a, b, width, height):
  return ((a[0] + b[0]) % width, (a[1] + b[1]) % height)


def move_blizzards(blizz, width, height):
  new_blizz = set()
  for c, dir in blizz:
    new_blizz.add((add_cord(c, dir, width, height), dir))
  return new_blizz


def in_bounds(c, w, h):
  return c[0] >= 0 and c[0] < w and c[1] >= 0 and c[1] < h


MOVE_DIR = [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]

def solve(start, end, blizz, width, height):
  
  q = [(start, 0)]
  visited = set()
  blizz_t = 0
  b = []
  while len(q) > 0:
    cur, t = q.pop(0)
    
    if (cur, t) in visited:
      continue

    visited.add((cur,t))

    if cur == end:
      return t, blizz
    
    if t > blizz_t:
      blizz = move_blizzards(blizz, width, height)
      b = [v[0] for v in blizz]
      blizz_t = t
      # print_blizz(blizz, width, height)
      # print(blizz_t)
    
    for d in MOVE_DIR:
      new_c = (cur[0] + d[0], cur[1] + d[1])

      if (not (new_c in b)) and (in_bounds(new_c, width, height) or new_c == start or new_c == end):
        q.append((new_c, t + 1))
    

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  blizz, start, end, w, h = read_input(open(argv[1]))
  print(w, h, start, end)

  blizz = move_blizzards(blizz, w, h)
  best, _ = solve(start, end, blizz, w, h)
  print('Shortest path:', best)

  print(round(time.time() - start_t, 3), 's')


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  blizz, start, end, w, h = read_input(open(argv[1]))
  print(w, h, start, end)

  blizz = move_blizzards(blizz, w, h)
  best_1, blizz = solve(start, end, blizz, w, h)
  print(best_1, round(time.time() - start_t, 3), 's')

  best_2, blizz = solve(end, start, blizz, w, h)
  print(best_2, round(time.time() - start_t, 3), 's')
  
  best_3, blizz = solve(start, end, blizz, w, h)
  print(best_3, round(time.time() - start_t, 3), 's')
  
  print('Shortest path:', best_1 + best_2 + best_3)

  print(round(time.time() - start_t, 3), 's')
