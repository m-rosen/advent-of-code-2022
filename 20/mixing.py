from sys import argv
import time

def read_input(f):
  nr = []
  i = 0
  for line in f:
    nr.append((int(line.strip()), i))
    i += 1
  return nr

def mix(file):
  file_len = len(file)
  for i in range(0, file_len):
    for idx, (nr, origin) in enumerate(file):
      if origin == i:
        new_index = (idx + nr) % (file_len - 1)

        if nr < 0: # moving left          
          if new_index == 0:
            new_index = file_len

        del file[idx]
        file.insert(new_index, (nr, origin))
        break
  
  i_0 = 0
  for i, (nr, origin) in enumerate(file):
    if nr == 0:
      i_0 = i
      break

  return file[(i_0 + 1000) % file_len][0] + file[(i_0 + 2000) % file_len][0] + file[(i_0 + 3000) % file_len][0]

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  t = time.time()
  file = read_input(open(argv[1]))
  print(mix(file))
  print(round(time.time() - t, 3) , 's')

''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  read_input(open(argv[1]))
  t = time.time()
  file = read_input(open(argv[1]))
  key = 811589153
  keyed_file = [(nr * key, i) for nr, i in file]
  for _ in range(0,10):
    res = mix(keyed_file)
  print(res)
  print(round(time.time() - t, 3) , 's')
