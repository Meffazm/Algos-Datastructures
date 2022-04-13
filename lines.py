from itertools import zip_longest


def lines(a):
    destroyed, idx = 0, 1
    while idx and len(a) > 2:
        for i, (x, y, z) in enumerate(zip_longest(a, a[1:], a[2:]), 1):
            if x == y and y == z:
                idx = i
                break
            idx = None
        if idx:
            left, right = 0, 0
            for _ in range(idx - 1, -1, -1):
                if a[_] == a[idx]:
                    left += 1
                else:
                    break
            for _ in range(idx + 1, len(a)):
                if a[_] == a[idx]:
                    right += 1
                else:
                    break
            destroyed += right + left + 1
            del a[idx-left:idx+right+1]
    return destroyed
