def edistance(A, B):
    n, m = len(A), len(B)
    D = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(0, n + 1):
        D[i][0] = i
    for j in range(0, m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
    return D[-1][-1]


def weighted_edistance(A, B, wdel, wins, wsub):
    n, m = len(A), len(B)
    D = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(0, n + 1):
        D[i][0] = i * wdel
    for j in range(0, m + 1):
        D[0][j] = j * wins
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = min(
                    D[i - 1][j] + wdel, D[i][j - 1] + wins, D[i - 1][j - 1] + wsub
                )
    return D[-1][-1]


def edistance_substring(A, B):
    n = len(A)
    m = len(B)
    D = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                D[i][j] = D[i - 1][j - 1]
            else:
                D[i][j] = 1 + min(D[i - 1][j], D[i][j - 1], D[i - 1][j - 1])
    return D[-1][-1]
