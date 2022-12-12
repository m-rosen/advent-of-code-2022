
from sys import stdin, argv
from collections import deque
from grid import Grid

def char_to_height(char):
  if char == 'S':
    return ord('a')

  elif char == 'E':
    return  ord('z')
  
  return ord(char)

def read_input():
  data = []
  start = None
  end = None

  for (j, line) in enumerate(stdin):
    line = line.strip()
    
    if 'S' in line:
      start = (j, line.index('S'))

    if 'E' in line:
      end = (j, line.index('E'))
    
    data.append([char_to_height(c) for c in line])
  return start, end, data

'''-------------------------------------------------------------------------'''

def can_climb(a, b, grid):
  return grid.in_bounds(b) and ((grid[b] - grid[a]) < 2)

def shortest_path(start, end, grid):
  visited = {}
  path = {start: [( start, 'S')]}
  q = deque() # [pos, distance]
  q.append((start, 0))

  while len(q) > 0:
    current = q.popleft()

    pos = current[0]
    dist = current[1]

    if pos == end:
      return (dist, path[end])

    if pos in visited:
      continue
    else:
      visited[pos] = dist

    elevation = grid[pos]
    
    # Add neighbours
    left  = (pos[0], pos[1] - 1)
    right = (pos[0], pos[1] + 1)
    up    = (pos[0] - 1, pos[1])
    down  = (pos[0] + 1, pos[1])

    if can_climb(pos, left, grid): # Left
      q.append([left, dist + 1])
      path[left] = path[pos] + [(pos, '<')]

    if can_climb(pos, right, grid): # Right
      q.append([right, dist + 1])
      path[right] = path[pos] + [(pos, '>')]

    if can_climb(pos, up, grid): # Up
      q.append([up, dist + 1])
      path[up] = path[pos] + [(pos, '^')]

    if can_climb(pos, down, grid): # Down
      q.append([down, dist + 1])
      path[down] = path[pos] + [(pos, 'v')]
  
  return (-1, []) # no path found

'''--------------------------------------------------------------------------'''

def print_path(start, end, path, width, height):
  path_grid = Grid(width, height, placeholder='.')
  for (pos, char) in path:
    path_grid[pos] = char

  path_grid[start] = 'S'
  path_grid[end] = 'E'

  print(path_grid)

'''--------------------------------------------------------------------------'''

if __name__ == "__main__" and len(argv) == 1:
  print("Part 1")
  start, end, data = read_input()
  grid = Grid(len(data[0]), len(data), data)

  length, path = shortest_path(start, end, grid)
  print("Shortest path has len:", length)
  print_path(start, end, path, grid.width, grid.height)


if __name__ == "__main__" and len(argv) > 1 and argv[1] == '2':
  print("Part 2")
  start, end, data = read_input()
  grid = Grid(len(data[0]), len(data), data)

  start_points = []
  for (j, row) in enumerate(data):
    for (i, v) in enumerate(row):
      if v == ord('a'):
        start_points.append((j,i))

  shortest = (grid.width*grid.height, [], None) # Data format: (length, path, start)
  for pos in start_points:
    length, path = shortest_path(pos, end, grid)

    if shortest:
      if shortest[0] > length and length > 0:
        shortest = (length, path, pos)
    else:
      shortest = (length, path, pos)

  print("Shortest path has len:", shortest[0])
  print_path(shortest[2], end, shortest[1], grid.width, grid.height)






  
