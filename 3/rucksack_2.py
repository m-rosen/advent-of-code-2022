
from sys import stdin

total = 0

for a in stdin:
  a.strip()
  b = stdin.readline().strip()
  c = stdin.readline().strip()

  for char in a:
    if char in b and char in c:
      val_low = ord(char) - ord('a')
      val_upp = ord(char) - ord('A')

      if val_low < 0:
        total += val_upp + 27
      else:
        total += val_low + 1
      
      break
  
print(total)
  