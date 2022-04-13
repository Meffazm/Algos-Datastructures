def dfs(v, visited, graph):
    visited[v] = True
    for vertex in graph[v]:
        if not visited[vertex]:
            dfs(vertex, visited, graph)


def minRooksLeft(board_size, coordinates):
    n = len(coordinates)
    rooks_left = 0
    adj_list = [[] for _ in range(n)]
    visited = [False for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and (coordinates[i][0] == coordinates[j][0] or coordinates[i][1] == coordinates[j][1]):
                adj_list[i].append(j)

    for vertex in range(n):
        if not visited[vertex]:
            rooks_left += 1
            dfs(vertex, visited, adj_list)

    return rooks_left


coords = [[0, 0], [0, 3], [3, 0]]
print(minRooksLeft(4, coords))
