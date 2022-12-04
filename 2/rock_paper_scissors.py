

from sys import stdin

score = 0
for line in stdin:

  # A = rock     = X
  # B = paper    = Y
  # C = scissors = Z

  # A == X, A < Y, A > Z
  # B == Y, B < Z, B > X
  # C == Z, C < X, C > Y

  L, R = line.split()

  if (R == 'X'):
    score += 1
  elif (R == 'Y'):
    score += 2
  else:
    score += 3

  if ((L,R) in [('A', 'X'), ('B', 'Y'), ('C', 'Z')]): # draw
    score += 3  
  elif ((L,R) in [('A', 'Y'), ('B', 'Z'), ('C', 'X')]): # win
    score += 6


print("SCORE:", score)