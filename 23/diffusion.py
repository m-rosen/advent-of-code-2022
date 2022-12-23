from sys import argv
import time

def read_input(f):
  elves = set()

  for y, line in  enumerate(f):
    for x, char in enumerate(line):
      if char == '#':
        elves.add((x, y))
  
  return elves

def find_bunding_box(elves):
  x_max = max(elves, key=lambda t: t[0])[0]
  x_min = min(elves, key=lambda t: t[0])[0]
  y_max = max(elves, key=lambda t: t[1])[1]
  y_min = min(elves, key=lambda t: t[1])[1]

  return ((x_min, y_min), (x_max, y_max))

def print_board(elves):
  min_pos, max_pos = find_bunding_box(elves)

  for y in range(min_pos[1], max_pos[1] + 1):
    line = ""
    for x in range(min_pos[0], max_pos[0] + 1):
      if (x,y) in elves:
        line += '#'
      else:
        line += '.'
    print(line)
  print()

# (x, y)
N =  ( 0, -1)
NE = ( 1, -1)
NW = (-1, -1)

S =  ( 0, 1)
SE = ( 1, 1)
SW = (-1, 1)

W =  (-1, 0)

E =  ( 1, 0)

MOVE_DIR = [ (N, NW, NE), (S, SW, SE), (W, NW, SW), (E, NE, SE) ]
CHECK_DIR = [ NW, N, NE, W, E, SW, S, SE ]

def pos_add(p1, p2):
  return (p1[0] + p2[0], p1[1] + p2[1])


def move(elves, round):
  next_pos = {}
  
  for e in elves:
    stay_still = True
    for d in CHECK_DIR:
      if pos_add(e, d) in elves:
        stay_still = False
        break
    
    if not stay_still:
      for d in range(round, round + 4):
        d1, d2, d3 = MOVE_DIR[d % 4]
        if pos_add(e, d1) not in elves and pos_add(e, d2) not in elves and pos_add(e, d3) not in elves:
          next_pos[e] = pos_add(e, d1)
          break

  elves_tmp = set()
  nr_moved = 0
  for e in elves:
    if e not in next_pos or sum(1 for v in next_pos.values() if v == next_pos[e]) > 1:
      elves_tmp.add(e)
    else:
      elves_tmp.add(next_pos[e])
      nr_moved += 1
  
  return elves_tmp, nr_moved


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  elves = read_input(open(argv[1]))
  # print_board(elves)
  for r in range(0, 10):
    elves, _ = move(elves, r)
    # print_board(elves)
  min_pos, max_pos = find_bunding_box(elves)
  area = abs(max_pos[0] - min_pos[0] + 1) * abs(max_pos[1] - min_pos[1] + 1)
  print(area - len(elves))

  print(round(time.time() - start_t, 3), 's')

''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  start_t = time.time()
  elves = read_input(open(argv[1]))
  
  r = 0
  nr_moved = 1
  while nr_moved > 0:
    elves, nr_moved = move(elves, r) 
    r += 1
    if r % 100 == 0:
      print(r)
      print(round(time.time() - start_t, 3), 's')

  print(r)
  print(round(time.time() - start_t, 3), 's')

