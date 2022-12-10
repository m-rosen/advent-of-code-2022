
from sys import stdin 

def draw_pixel(pixels, cycle, x):
  row = cycle // 40
  col = cycle % 40

  if x >= col -1 and x <= col + 1:
    pixels[row][col] = '#'

x = 1
cycle = 0

pixels = [['.' for i in range(0,40)] for j in range(0,6)]
row = 0
col = 0

for line in stdin:
  line = line.strip()

  draw_pixel(pixels, cycle, x)
  cycle += 1


  instr = line[0:4]
  if instr == "addx":
    draw_pixel(pixels, cycle, x)
    cycle += 1

    _ , v = line.split()
    x += int(v)


for row in pixels:
  line = ""
  for col in row:
    line += col
  print(line)