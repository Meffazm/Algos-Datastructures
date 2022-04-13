def calc_rain_water(h):
    column_heights, result = [], 0
    local_maxima, last_maxima, local_maxima_id = None, None, None

    if h[0] >= h[1]:
        local_maxima, local_maxima_id = h[0], 0

    if h[-1] >= h[-2]:
        last_maxima = h[-1]

    for i in range(1, len(h) - 1):
        if h[i] >= h[i - 1] and h[i] >= h[i + 1]:
            if not local_maxima:
                local_maxima, local_maxima_id = h[i], i
            else:
                level = min(local_maxima, h[i])
                result += sum((level - column) * (level > column) for column in column_heights)
                local_maxima, local_maxima_id = h[i], i
                column_heights.clear()
        else:
            column_heights.append(h[i])

    if last_maxima:
        level = min(local_maxima, h[-1])
        result += sum((level - column) * (level > column) for column in h[local_maxima_id + 1:-1])

    return result
