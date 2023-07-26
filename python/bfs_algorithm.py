def bfs (grid):
  visited = []
  i, j = 0,0
  queue = [[i,j]]
  visited.append([i,j])
  m = len(grid)
  n = len(grid[0])
  while queue:
      removed_node = queue.pop(0)
      i = removed_node[0]
      j = removed_node[1]            
      if i+1 < m:
          if [i+1, j] not in visited:
              queue.append([i + 1, j])
              visited.append([i + 1, j])
      if j+1 < n:
          if [i, j+1] not in visited:
              queue.append([i, j+1])
              visited.append([i, j+1])
