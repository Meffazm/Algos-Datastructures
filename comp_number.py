graph = []
visited = []


def dfs(v):
    visited[v] = True
    for vertex, edge in enumerate(graph[v]):
        if edge == 1 and not visited[vertex]:
            dfs(vertex)


def sameComponent(adj_list, vertex):
    global graph, visited
    graph = adj_list
    n = len(graph)
    visited = [False for _ in range(n)]
    dfs(vertex)
    return sum(visited)