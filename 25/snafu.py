from sys import argv
import time

def read_input(f):
  data = []
  for line in f:
    data.append(line.strip())
  return data
  
S_to_D = {'2':  2, '1':  1, '0':  0,  '-': -1,  '=': -2  }
D_to_S = { 2 : '2', 1 : '1', 0 : '0', -1 : '-', -2 : '=' }

def snafu_to_dec(s):
  place = len(s) - 1
  d = 0
  for c in s:
    d += S_to_D[c] * (5 ** place)
    place -= 1
  
  return d

def dec_to_snafu(d):
  pent = []
  while d > 0:
    r = d % 5
    pent.append(r)
    d //= 5

  snafu = pent + [0]

  for i in range(0, len(pent)):
    c = snafu[i]
    if c == 5:
      snafu[i + 1] += 1
      snafu[i] = 0
    elif c == 4:
      snafu[i + 1] += 1
      snafu[i] = -1
    elif c == 3:
      snafu[i + 1] += 1
      snafu[i] = -2

  if snafu[-1] == 0:
    snafu.pop()
  snafu.reverse()
  res = ''
  for c in snafu:
    res += D_to_S[c]
  return res


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  data = read_input(open(argv[1]))

  sum = 0
  for s in data:
    sum += snafu_to_dec(s)
  
  print(sum, dec_to_snafu(sum))

  print(round(time.time() - start_t, 3), 's')

