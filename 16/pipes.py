from sys import argv
import time

def read_input(f):
  i = 0
  valve = {} # key : value -> name : (idx, capacity)
  for line in f:
    token = line.split()
    val = token[1]
    cap = int(token[4].split('=')[1].strip(';'))
    
    valve[val] = (i, cap)
    i += 1

  f.seek(0)
  edge = []
  for line in f:
    token = line.split()
    val = token[1]
    neigbours = [n.strip(',') for n in token[9:]]
    
    for n in neigbours:
      edge.append((valve[val][0], valve[n][0]))
  
  return valve, edge


''' Floyd warshall's algorithm '''
def shortest_paths(edges, nr_nodes):
  inf =  2 * nr_nodes
  dist = [[inf for _ in range(0, nr_nodes)] for _ in range(0, nr_nodes)]

  for (u,v) in edges:
    dist[u][v] = 1
  
  for v in range(0, nr_nodes):
    dist[v][v] = 0
  
  for k in range(0, nr_nodes):
    for i in range(0, nr_nodes):
        for j in range(0, nr_nodes):
            if dist[i][j] > (dist[i][k] + dist[k][j]):
              dist[i][j] = dist[i][k] + dist[k][j]
  return dist


''' Find the optimal order to visit the valves '''
def solve(cur, time_left, closed, valve, path):
  if time_left > 1:
    total_flow = valve[cur][1] * (time_left - 1)
    best_path = []
    if len(closed) > 0:
      best = 0
      for next in closed:
        closed_copy = [v for v in closed if v != next]
        travel_time = path[valve[cur][0]][valve[next][0]]
        flow, sub_path = solve(next, time_left - travel_time - 1, closed_copy, valve, path)
        if flow > best:
          best_path = sub_path
        best = max(best, flow)
      total_flow += best
    return total_flow, [cur] + best_path
  return 0, []


''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  start_t = time.time()
  valve, edges = read_input(open(argv[1]))

  path = shortest_paths(edges, len(valve))
  print("Paths found")
  print(round(time.time() - start_t, 3), 's')

  non_zero_valves = [ v for v, info in valve.items() if info[1] > 0]
  res, p = solve("AA", 31, non_zero_valves, valve, path)
  print(res, p)
  print(round(time.time() - start_t, 3), 's')
