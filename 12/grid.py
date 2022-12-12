

class Grid:
  def __init__(self, width, height, items = None, placeholder = 0):
    self.width = width
    self.height = height
    if items:
      self.grid = items
    else:
      self.grid = [[placeholder for _ in range(0, width)] for _ in range(0, height)]
  
  def __str__(self):
    s = ""
    for row in self.grid:
      line = ""
      for item in row:
        line += str(item) + " "
      s += line + "\n"
    return s

  def in_bounds(self, pos):
    return pos[0] >= 0 and pos[0] < self.height \
      and pos[1] >= 0 and pos[1] < self.width

  def __getitem__(self, pos):
    if self.in_bounds(pos):
      return self.grid[pos[0]][pos[1]]

  def __setitem__(self, pos, val):
    if self.in_bounds(pos):
      self.grid[pos[0]][pos[1]] = val


  def neighbours(self, pos):
    left  = (pos[0], pos[1] - 1)
    right = (pos[0], pos[1] + 1)
    up    = (pos[0] - 1, pos[1])
    down  = (pos[0] + 1, pos[1])

    return [n for n in [left, right, up, down] if self.in_bounds(n)]

