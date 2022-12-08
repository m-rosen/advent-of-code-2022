
from sys import stdin

grid = []

for line in stdin:
  line = line.strip()
  row = [int(c) for c in line]
  grid.append(row)

height = len(grid)
width = len(grid[1])

high_score = 1

for j in range(0, height):
  for i in range(0, width):
    row = grid[j]
    col = [line[i] for line in grid]
    tree = grid[j][i]

    # Check tree from all four directions
    dir = []
    dir.append(col[j-1::-1] if j > 0 else [])  # above
    dir.append(col[j+1:height])  # below
    dir.append(row[i-1::-1] if i > 0 else [])  # left
    dir.append(row[i+1: width])  # right

    score = 1
    for d in dir:
      found_blocking = False
      for (i, t) in enumerate(d):
        if t >= tree:
          score *= i + 1
          found_blocking = True
          break
      
      if not found_blocking:
        score *= len(d)

    high_score = max(score, high_score)

print(high_score)