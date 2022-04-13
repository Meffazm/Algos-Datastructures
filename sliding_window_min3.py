from itertools import islice, tee, count, repeat

def sliding_window_min(a, k):
    return list(map(min, *(map(islice, tee(a, k), count(), repeat(None)))))
