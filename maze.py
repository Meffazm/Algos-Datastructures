from math import inf


# ------------------------------------------------ Task 1 -------------------------------------------------------
def fastest_escape_length(maze, i=0, j=0, short_len=1):
    n, m, result = len(maze), len(maze[0]), inf  # size of maze and result init

    # base condition
    if i == n - 1 and j == m - 1:  # reached way out
        return short_len

    maze[i][j] = 1  # block way out

    # main body
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:  # going top, left, down, right
        
        if 0 <= a < n and 0 <= b < m and maze[a][b] == 0:  # maze boundaries and passage check
            result = fastest_escape_length(maze, a, b, short_len=short_len + 1)

    maze[i][j] = 0  # restore passage

    return result


# ------------------------------------------------ Task 2 -------------------------------------------------------
def fastest_escapes(maze):  # wrapper function

    short_len = fastest_escape_length(maze)  # find shortest escape length

    def fastest_escapes_wrapped(maze_inner, i=0, j=0, length=1, esc_paths=None, cur_path=None):
        if cur_path is None:
            cur_path = [(0, 0)]  # setting initaial current path as starting point
        if esc_paths is None:
            esc_paths = []  # empty list of all shortest paths init
        n, m, result = len(maze_inner), len(maze_inner[0]), False  # size of maze and result init

        # base condition
        if i == n - 1 and j == m - 1 and length == short_len:  # reached way out and path is shortest
            esc_paths.append(cur_path)
            return esc_paths

        maze_inner[i][j] = 1  # block way out

        # main body
        for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:  # going top, left, down, right

            if 0 <= a < n and 0 <= b < m and maze_inner[a][b] == 0:  # maze boundaries and passage check
                esc_paths = fastest_escapes_wrapped(maze_inner, a, b, length=length + 1,
                                                    esc_paths=esc_paths, cur_path=cur_path + [(a, b)])

        maze_inner[i][j] = 0  # restore passage

        return esc_paths

    return fastest_escapes_wrapped(maze)


# ------------------------------------------------ Task 3 -------------------------------------------------------
def weighted_escape_length(maze, w, i=0, j=0, short_len=1, wall=False):
    n, m = len(maze), len(maze[0])  # size of maze
    result_wall = result_passage = inf  # results init

    # base condition
    if i == n - 1 and j == m - 1:
        return short_len

    maze[i][j] = 2  # block way out

    # main body
    for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:  # going top, left, down, right
        if 0 <= a < n and 0 <= b < m:  # maze boundaries check

            if maze[a][b] == 1:  # go through wall
                result_wall = weighted_escape_length(maze, w, a, b, short_len=short_len + w, wall=True)
            elif maze[a][b] == 0:  # go through passage
                result_passage = weighted_escape_length(maze, w, a, b, short_len=short_len + 1)

    if wall:
        maze[i][j] = 1  # restore wall
    else:
        maze[i][j] = 0  # restore passage

    return min(result_wall, result_passage)


# ------------------------------------------------ Task 4 -------------------------------------------------------
def weighted_escapes(maze, w):  # wrapper function

    weight_len = weighted_escape_length(maze, w)  # find shortest escape length with weights

    def weight_escapes_wrapped(inner_maze, w_inner, i=0, j=0, length=1, esc_paths=None, cur_path=None, wall=False):
        if cur_path is None:
            cur_path = [(0, 0)]  # setting initaial current path as starting point
        if esc_paths is None:
            esc_paths = []  # empty list of all shortest paths init
        n, m = len(inner_maze), len(inner_maze[0])  # size of maze

        if i == n - 1 and j == m - 1 and length == weight_len:  # reached way out and path is shortest
            esc_paths.append(cur_path)
            return esc_paths

        inner_maze[i][j] = 2  # block way out

        # main body
        for a, b in [(i - 1, j), (i, j - 1), (i + 1, j), (i, j + 1)]:  # going top, left, down, right
            if 0 <= a < n and 0 <= b < m:  # maze boundaries check

                if maze[a][b] == 1:  # go through wall
                    esc_paths = weight_escapes_wrapped(inner_maze, w_inner, a, b, length=length + w_inner,
                                                       esc_paths=esc_paths, cur_path=cur_path + [(a, b)], wall=True)
                elif maze[a][b] == 0:  # go through passage
                    esc_paths = weight_escapes_wrapped(inner_maze, w_inner, a, b, length=length + 1,
                                                       esc_paths=esc_paths, cur_path=cur_path + [(a, b)])

        if wall:
            inner_maze[i][j] = 1  # restore wall
        else:
            inner_maze[i][j] = 0  # restore passage

        return esc_paths

    return weight_escapes_wrapped(maze, w)


# test_my = [
#     [0, 1, 0, 0, 0, 0],
#     [0, 1, 0, 1, 1, 0],
#     [0, 1, 0, 0, 1, 0],
#     [0, 0, 1, 0, 1, 0],
#     [1, 0, 0, 0, 1, 0]
# ]
# print(weighted_escape_length(test_my, 2))

test_a = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]
test_b = [
    [0, 0, 0],
    [1, 1, 1],
    [0, 0, 0]
]
# should print 2
print(weighted_escape_length(test_a, 0))

# should print 5
print(weighted_escape_length(test_b, 1))

# should print 6
print(weighted_escape_length(test_b, 2))
