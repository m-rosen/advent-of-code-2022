from sys import argv

def read_input(f):
  return f.readline().strip()

SHAPE = [
  [(0,0), (1,0),(2,0), (3,0)], # --
  [(1,0), (0,1), (1,1), (2,1), (1,2)], # +
  [(0,0), (1,0), (2,0), (2,1), (2,2)], # (backwards) L
  [(0,0), (0,1), (0,2), (0,3)], # I
  [(0,0), (1,0), (0,1), (1,1)] # o
]

DX = { '>': 1, '<': -1 }

def print_board(top, blocks):
  for row in range(top, -1, -1):
    line = '|'
    for col in range(0,7):
      if (col, row) in blocks:
        line += '#'
      else:
        line += '.'
    print(line + '|')
  print('+-------+')

def can_move(shape_idx, pos, blocks, dim):
  for cord in SHAPE[shape_idx]:
    new_pos = (cord[0] + pos[0], cord[1] + pos[1])
    if new_pos[dim] < 0 or (dim == 0 and new_pos[dim] >= 7) or new_pos in blocks:
      return False
  return True

def move(dir, shape, pos, blocks):
  # Move left/right
  new_pos = (pos[0]+DX[dir], pos[1]) 
  if can_move(shape, new_pos, blocks, 0):
    pos = new_pos
  
  # Fall
  stopped = False
  top_y = 0
  new_pos = (pos[0], pos[1] - 1) 
  if can_move(shape, new_pos, blocks, 1):
    pos = new_pos
  else:
    stopped = True
    for cord in SHAPE[shape]:
      blocks.add((cord[0] + pos[0], cord[1] + pos[1]))
    top_y = SHAPE[shape][-1][1] + pos[1] + 1  
  return stopped, pos, top_y

def solve(steam):
  top = 0
  time = 0
  blocks = set()
  for rock in range(0, 2022):
    pos = (2, top + 3)
    stopped = False
    while not stopped:
      stopped, new_pos, block_top = move(steam[time%len(steam)], rock % 5, pos, blocks)
      pos = new_pos
      top = max(top, block_top)
      time += 1

  return top

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  steam = read_input(open(argv[1]))
  print(solve(steam))
