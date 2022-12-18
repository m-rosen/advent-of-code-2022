from sys import argv

def read_input(f):
  graph = {} # key : value ->  'AA' : (flow, neighbous[])
  
  for line in f:
    token = line.split()
    valve = token[1]
    flow = int(token[4].split('=')[1].strip(';'))
    neigbours = [n.strip(',') for n in token[9:]]

    graph[valve] = (flow, neigbours)
  
  return graph


def path_len(src, dst, g, visited = []):
  if src == dst:
    return 0

  if dst in g[src][1]:
    return 1

  inf = 2*len(g)
  steps = inf
  
  for n in g[src][1]:
    if n not in visited:
      p = path_len(n, dst, g, visited + [src])
      if p == None:
        continue
      steps = min(p, steps)
  
  if steps < inf:
    return steps + 1

''' Find the optimal order to visit the valves '''
def solve(cur, time_left, valves, g, path):
  if time_left > 1:
    total_flow = g[cur][0] * (time_left - 1)
    best_path = []
    if len(valves) > 0:
      best = 0
      for next in valves:
        valve_copy = [v for v in valves if v != next]
        flow, sub_path = solve(next, time_left - path[(cur, next)] - 1, valve_copy, g, path)
        if flow > best:
          best_path = sub_path
        best = max(best, flow)
      total_flow += best
    return total_flow, [cur] + best_path
  return 0, []

''' Part 1 '''
if __name__ == "__main__" and len(argv) == 2:
  g = read_input(open(argv[1]))

  path = {}
  for u in g:
    for v in g:
      path[(u,v)] = path_len(u, v, g)
      path[(v,u)] = path[(u,v)]
  
  non_zero_valves = [ v for v in g if g[v][0] > 0]
  res, p = solve("AA", 31, non_zero_valves, g, path)
  print(res, p)


def solve_2(me, ele, t_m, t_e, valves, g, path):
  if t_m > 1 or t_e > 1:
    total_flow = max(g[me][0] * (t_m - 1), 0)
    total_flow += max(g[ele][0] * (t_e - 1), 0)
    if len(valves) > 0:
      best = 0
      for m_next in valves:
        for e_next in valves:
          if m_next != e_next:
            valve_copy = [v for v in valves if v != m_next and v != e_next]
            flow = solve_2(m_next, e_next, t_m - path[(me, m_next)] - 1, t_e - path[(ele, e_next)] - 1, valve_copy, g, path)
            best = max(best, flow)
      total_flow += best
    return total_flow
  return 0

''' Part 2 '''
if __name__ == "__main__" and len(argv) == 3 and argv[2] == '2':
  g = read_input(open(argv[1]))

  path = {}
  for u in g:
    for v in g:
      path[(u,v)] = path_len(u, v, g)
      path[(v,u)] = path[(u,v)]
  
  non_zero_valves = [ v for v in g if g[v][0] > 0]
  res = solve_2("AA", "AA", 27, 27, non_zero_valves, g, path)
  print(res)
