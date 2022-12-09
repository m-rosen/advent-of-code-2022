
from sys import stdin

def print_grid(visited, knots= []):
  (_, min_x) = min(visited, key = lambda x: x[1])
  (_, max_x) = max(visited, key = lambda x: x[1])
  (min_y, _) = min(visited, key = lambda x: x[0])
  (max_y, _) = max(visited, key = lambda x: x[0])
  
  print()

  for j in range(max_y, min_y - 1, -1):
    row = ""
    for i in range(min_x, max_x + 1):
      if [j, i] in knots:
        row += str(knots.index([j,i]))
      elif (j,i) in visited:
        row += '#'
      else:
        row += '.'
    print(row)

'''--------------------------------------------------------------------------'''

def move(dir, knots):
  H = knots[0]
  if dir == 'L':
    H[1] -= 1
  elif dir == 'R':
    H[1] += 1
  elif dir == 'U':
    H[0] += 1
  elif dir == 'D':
    H[0] -= 1


  for (i, prev) in enumerate(knots[:-1]):
    current = knots[i + 1]  

    dy = prev[0] - current[0]
    dx = prev[1] - current[1]

    
    if ((abs(dy) > 1 and abs(dx) >= 1) or (abs(dy) >= 1 and abs(dx) > 1)): # Move diagonally
      current[0] += 1 if dy > 0 else -1
      current[1] += 1 if dx > 0 else -1
      
    elif (abs(dy) > 1): # Move vertically
      current[0] += 1 if dy > 0 else -1
      
    elif (abs(dx) > 1): # Move horizontally
      current[1] += 1 if dx > 0 else -1

'''--------------------------------------------------------------------------'''

# Main program

visited = set()

nr_knots = 2 # First part
# nr_knots = 10 # Second part

knots = [[0,0] for i in range(0, nr_knots)] # [row, col]

visited.add((0,0))

for line in stdin:
  dir, dist = line.strip().split()
  dist = int(dist)

  for _ in range(0, dist):
    move(dir, knots)
    visited.add((*knots[-1],))

print_grid(visited, knots)
print(len(visited))