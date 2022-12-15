from sys import argv

def read_input(file):
  sensor = {}
  for line in file:
    l, r = line.split(':')
    x, y = [ int(s.split('=')[1].strip(',')) for s in l.split(' ') if '=' in s ]
    x_b, y_b = [ int(s.split('=')[1].strip(',')) for s in r.split(' ') if '=' in s ]
    
    sensor[(x,y)] = (x_b, y_b)
    
  return sensor


def sensor_range(item):
  sensor, beacon = item
  return  abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])


def print_beacons(data):
  x_min = min([item[0][0] + sensor_range(item) for item in data.items()])
  x_max = max([item[0][0] + sensor_range(item) for item in data.items()])

  y_min = min([item[0][1] + sensor_range(item) for item in data.items()])
  y_max = max([item[0][1] + sensor_range(item) for item in data.items()])
  
  s = data.keys()
  b = data.values()

  for j in range(y_min, y_max + 1):
    row = ""
    for i in range(x_min, x_max + 1):
      if (i, j) in s:
        row += 'S'
      elif (i, j) in b:
        row += 'B'
      else:
        row += '.'
    print(row)


def find_coverage(row, item, cov):
  sensor, beacon = item
  reach = sensor_range(item)
  dy = abs(sensor[1] - row)
  reach -= dy

  if reach <= 0:
    return

  interval = (sensor[0] - reach, sensor[0] + reach)
  cov.append(interval)


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  sensor = read_input(open(argv[1]))
  
  cov = []
  row = 2000000
  for item in sensor.items():
    find_coverage(row, item, cov)  
  cov.sort()

  count = 0
  x = cov[0][0]
  for interval in cov:
    start, end = interval
    start = max(x, start)
    end = max(x, end)
    count += end - start
    x = end
  
  print(count)


''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  sensor = read_input(open(argv[1]))

  lim = 4000000
  beacons = sensor.values()
  percent = 0
  for row in range(0, lim + 1):
    if row % (lim // 10) == 0:
      percent += 10
      print(percent, "%")
  
    cov = []
    for item in sensor.items():
      find_coverage(row, item, cov)  
    cov.sort()
    
    count = 0
    x = 0
    for interval in cov:
      start, end = interval
      start = max(x, start)
      end = max(x, end)
      count += end - start

      for i in range(1, start - x):  # detected gap
        if (x + i, row) in beacons:
          count += 1
        else:
          print((x + i, row), (x + i) * 4000000 + row)
          exit(0)
      
      x = end
      if x >= lim:
        break
      
    
    if count < lim: # if not entire row covered
      print(count, (x, row), x * 4000000 + row)
      exit(0)

