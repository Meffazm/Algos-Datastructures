import math


def find_percentile(a, b, p):
    """
    Main/wrapper function

    a, b - two sorted arrays
    p - percentile
    """

    # compute ordinal rank, which is (percentile index + 1) in combined Array c
    ord_rank = int(math.ceil(((len(a) + len(b)) * p) / 100))

    def _find_percentile(a_start, b_start, cur_split, _a=a, _b=b):
        """
        Auxiliary/wrapped function

        a_start, b_start - pointers where new subarrays of a,b start;
        cur_split - current split point for two arrays
        _a, _b - inner variables for arrays a, b which do not change, so we set them as default
        """

        # base case:
        # 1. a is empty or start of subarray reached the end of a, so a can be discarded totally
        if a_start == len(_a):
            return _b[b_start + cur_split]
        # 2. b is empty or start of subarray reached the end of b, so b can be discarded totally
        elif b_start == len(_b):
            return _a[a_start + cur_split]
        # 3. percentile is zero or cannot split arrays more
        elif cur_split == 0:
            return min(_a[a_start], _b[b_start])

        # find new split in a, first part in case our current subarray of a is less then cur_split
        a_split = min(len(_a) - a_start, (cur_split + 1) // 2)
        # find new split in b, first part in case our current subarray of b is less then cur_split
        b_split = min(len(_b) - b_start, (cur_split + 1) // 2)

        # discarding too small values in one of arrays
        # compare values at split pointers of current subarrays
        # "-1" because indexing starts at 0
        if _a[a_start + a_split - 1] < _b[b_start + b_split - 1]:
            # discard the part to the left of a_split in Array a as too small and shift cur_split by a_split value
            return _find_percentile(a_start + a_split, b_start, cur_split - a_split)
        # discard the part to the left of b_split in Array b as too small and shift cur_split by b_split value
        return _find_percentile(a_start, b_start + b_split, cur_split - b_split)

    # we start with subarrays a[0:ord_rank-1], b[0:ord_rank-1], other parts are discarded
    # "-1" because indexing starts at 0
    return _find_percentile(0, 0, ord_rank - 1)
