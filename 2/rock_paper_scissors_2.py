

from sys import stdin

score = 0
for line in stdin:

  # A = rock     = X
  # B = paper    = Y
  # C = scissors = Z

  # X = lose
  # Y = draw
  # Z = win

  # A == X, A < Y, A > Z
  # B == Y, B < Z, B > X
  # C == Z, C < X, C > Y

  L, R = line.split()

  if (R == 'X'): # lose
    if (L == 'A'):
      score += 3 
    elif (L == 'B'):
      score += 1
    else:
      score += 2

  elif(R == 'Y'): # draw 
    score += 3
    if (L == 'A'):
      score += 1 
    elif (L == 'B'):
      score += 2
    else:
      score += 3

  else: # win
    score += 6
    if (L == 'A'):
      score += 2 
    elif (L == 'B'):
      score += 3
    else:
      score += 1


print("SCORE:", score)