def calc_rain_water(h):

    left_cols, right_cols = [0] * len(h), [0] * len(h)
    left_cols[0], right_cols[-1] = h[0], h[-1]
    res = 0

    for i in range(1, len(h)):
        left_cols[i] = max(left_cols[i - 1], h[i])
    for i in range(len(h) - 2, -1, -1):
        right_cols[i] = max(right_cols[i + 1], h[i])
    for i in range(len(h)):
        res += min(left_cols[i], right_cols[i]) - h[i]

    return res
