def calc_rain_water(h):

    heights, cur_maxima, rise, res = [h[0]], None, None, 0

    for height in h[1:]:
        if rise is None and height < heights[-1]:
            cur_maxima = heights.pop()
            heights.clear()
            rise = False
        elif height < heights[-1] and rise:
            if not cur_maxima:
                cur_maxima = heights.pop()
                heights.clear()
                rise = False
            else:
                level = min(heights[-1], cur_maxima)
                res += sum(level - height for height in heights if level > height)
                cur_maxima = heights.pop()
                heights.clear()
                rise = False
        elif height > heights[-1]:
            rise = True
        elif height < heights[-1]:
            rise = False

        heights.append(height)

    if rise:
        level = min(heights[-1], cur_maxima)
        res += sum(level - height for height in heights if level > height)

    return res
