from collections import deque


def sliding_window_min(a, k):
    Q = deque()
    n = len(a)
    result = []
    for i in range(k):
        while Q and a[i] <= a[Q[-1]]:
            Q.pop()
        Q.append(i)
    for i in range(k, n):
        result.append(a[Q[0]])
        while Q and Q[0] <= i - k:
            Q.popleft()
        while Q and a[i] <= a[Q[-1]]:
            Q.pop()
        Q.append(i)
    result.append(a[Q[0]])
    return result
