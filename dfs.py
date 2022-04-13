def dfs(v):
  visited[v] = True
  for vertex, edge in enumerate(graph[v]):
    if edge == 1 and not visited[vertex]:
      dfs(vertex)