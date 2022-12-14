from sys import argv

def print_map(walls, sand = {(500,0)}):
  x_max = max(max(walls, key=lambda x: x[0])[0], max(sand, key=lambda x: x[0])[0])
  x_min = min(min(walls, key=lambda x: x[0])[0], min(sand, key=lambda x: x[0])[0])
  y_max = max(max(walls, key=lambda x: x[1])[1], max(sand, key=lambda x: x[1])[1])
  y_min = min(min(walls, key=lambda x: x[1])[1], min(sand, key=lambda x: x[1])[1])

  for j in range(y_min, y_max + 1):
    row = ""
    for i in range(x_min, x_max + 1):
      if (i, j) in walls:
        row += '#'
      elif (i, j) in sand:
        row += 'o'
      else:
        row += '.'
    print(row)


def read_walls():
  walls = set()

  f = open(argv[1])
  for line in f:
    str_points = line.strip().split('->')
    points = []
    for p in str_points:
      (x,y) = [int(n) for n in p.split(',')]
      points.append((x,y))

    for i, start in enumerate(points[:-1]):
      p = start
      next = points[i+1]

      dx = next[0] - start[0]
      if dx < 0: # -> up
        dx = -1
      elif dx > 0: # -> down
        dx = 1

      dy = next[1] - start[1]
      if dy < 0: # -> left
        dy = -1
      elif dy > 0: # -> right
        dy = 1

      while p != next:
        walls.add(p)
        p = (p[0] + dx, p[1] + dy)
      
      walls.add(next)

  return walls


def move(pos, walls, sand):
  down = (pos[0], pos[1] + 1)
  down_left = (pos[0] - 1, pos[1] + 1)
  down_right = (pos[0] + 1, pos[1] + 1)
  
  if down not in walls and down not in sand:
    return down
  elif down_left not in walls and down_left not in sand:
    return down_left
  elif down_right not in walls and down_right not in sand:
    return down_right
  else:
    return None

def add_sand(walls, sand, max_depth):
  s = (500, 0)

  while (next := move(s, walls, sand)):
    s = next
    if s[1] > max_depth:
      return False

  if s == (500, 0):
    return False
  
  sand.add(s)
  return True


if __name__ == '__main__' and len(argv) == 2:
  walls = read_walls()

  _, y_max = max(walls, key=lambda x: x[1])
  sand = set()
  count = 0
  while add_sand(walls, sand, y_max):
    pass

  print_map(walls, sand)
  print(len(sand))


def add_sand_2(walls, sand, max_depth):
  s = (500, 0)

  while (next := move(s, walls, sand)):
    s = next
    if s[1] == max_depth:
      break

  sand.add(s)
  if s == (500, 0):
    return False
  return True

if __name__ == '__main__' and len(argv) == 3 and argv[2] == '2':
  walls = read_walls()

  _, y_max = max(walls, key=lambda x: x[1])
  sand = set()
  while add_sand_2(walls, sand, y_max + 1):
    pass

  print_map(walls, sand)
  print(len(sand))