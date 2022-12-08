
from sys import stdin

grid = []

for line in stdin:
  line = line.strip()
  row = [int(c) for c in line]
  grid.append(row)

height = len(grid)
width = len(grid[1])

nr_visible = 0

for j in range(0, height):
  for i in range(0, width):
    row = grid[j]
    col = [line[i] for line in grid]
    tree = grid[j][i]
    
    # Check tree from all four directions
    dir = []
    dir.append(col[0: j])        # above
    dir.append(col[j+1:height])  # below
    dir.append(row[0: i])        # left
    dir.append(row[i+1: width])  # right

    for d in dir:
      if len(list(filter(lambda x: x >= tree, d))) == 0:
        nr_visible += 1
        break

print(nr_visible)