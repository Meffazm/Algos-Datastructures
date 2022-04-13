import math


def tj_cost(L, W):
    n = len(W)
    tbl = [math.inf for _ in range(n + 1)]
    splt = [0 for _ in range(n + 1)]
    tbl[0] = 0

    for i in range(1, n + 1):
        length = -1

        for j in range(i - 1, -1, -1):

            length += 1 + len(W[j])
            if length > L:
                P = math.inf
            else:
                if i == n:
                    P = 0
                else:
                    P = (L - length) ** 3

            if tbl[j] + P < tbl[i]:
                tbl[i] = tbl[j] + P
                splt[i] = j

    return tbl[-1]


def tj(L, W):
    last = n = len(W)
    tbl = [math.inf for _ in range(n + 1)]
    splt = [0 for _ in range(n + 1)]
    tbl[0] = 0
    ans = []

    for i in range(1, n + 1):
        length = -1

        for j in range(i - 1, -1, -1):

            length += 1 + len(W[j])
            if length > L:
                P = math.inf
            else:
                if i == n:
                    P = 0
                else:
                    P = (L - length) ** 3

            if tbl[j] + P < tbl[i]:
                tbl[i] = tbl[j] + P
                splt[i] = j

    while last > 0:
        ans.append(W[splt[last]: last])
        last = splt[last]

    return '\n'.join([' '.join(s) for s in ans[::-1]])
