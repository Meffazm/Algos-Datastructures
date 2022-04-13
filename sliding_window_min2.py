from collections import deque
from itertools import islice


def sliding_window_min(a, k):
    seq = iter(a)
    res = []
    d = deque(islice(seq, k), k)
    while True:
        try:
            res.append(min(d))
            d.append(next(seq))
        except StopIteration:
            return res




if __name__ == "__main__":
    test_a, test_k = [1, 3, 4, 5, 2, 7], 3
    # should print [1, 3, 2, 2]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [5, 4, 10, 1], 2
    # should print [4, 4, 1]
    print(sliding_window_min(test_a, test_k))

    test_a, test_k = [10, 20, 6, 10, 8], 5
    # should print [6]
    print(sliding_window_min(test_a, test_k))


