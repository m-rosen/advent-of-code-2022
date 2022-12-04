
from sys import stdin

total = 0

for line in stdin:
  nr_items = len(line.strip()) 
  
  a = line[0:nr_items//2]
  b = line[nr_items//2::]

  for char in a:
    if char in b:
      val_low = ord(char) - ord('a')
      val_upp = ord(char) - ord('A')

      if val_low < 0:
        total += val_upp + 27
      else:
        total += val_low + 1
      
      break
  
print(total)
  