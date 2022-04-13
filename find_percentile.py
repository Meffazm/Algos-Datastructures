import math
from random import randint, seed
from timeit import timeit


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


def test_find_percentile(a, b, p, correct_answer):
    tested = find_percentile(a, b, p)
    error_str = f'Test failed!\nInput: {a}, {b}, {p}\nOutput:{tested}\nCorrect output: {correct_answer}'
    assert tested == correct_answer, error_str


def run_unit_tests():
    test_find_percentile([1, 2, 7, 8, 10], [6, 12], 50, 7)
    test_find_percentile([1, 2, 7, 8], [6, 12], 50, 6)
    test_find_percentile([15, 20, 35, 40, 50], [], 30, 20)
    test_find_percentile([15, 20], [25, 40, 50], 40, 20)
    print('All unit tests passed!')


# reference solution
def find_percentile_naive(a, b, p):
    c = sorted(a + b)
    ord_rank = int(math.ceil(((len(a) + len(b)) * p) / 100))
    return c[ord_rank-1]


def get_rangom_test(max_size, max_value):
    # at least one of arrays should be not empty, let it be a
    a = sorted([randint(0, max_value) for _ in range(randint(0, max_size) + 1)])
    b = sorted([randint(0, max_value) for _ in range(randint(0, max_size))])
    p = randint(1, 100)
    return a, b, p


def run_stress_test(max_test_size=10, max_max_value=20, max_attempts=1000):
    seed(100)
    for test_size in range(1, max_test_size):
        for max_value in range(max_max_value):
            for _ in range(max_attempts):
                a, b, p = get_rangom_test(test_size, max_value)
                ans = find_percentile(a, b, p)
                ref_ans = find_percentile_naive(a, b, p)
                error_str = f'Test failed!\nInput: {a}, {b}, {p}\nOutput:{ans}\nCorrect output: {ref_ans}'
                assert ans == ref_ans, error_str
    print('All stress tests passed!')


def get_max_test(max_value=20000, size=10**6):
    seed(100)
    a = sorted([randint(0, max_value) for _ in range(size)])
    b = sorted([randint(0, max_value) for _ in range(size)])
    p = randint(1, 100)
    return a, b, p


# The algorithm worked for 0.000020726 seconds
def run_max_test(exec_times=100000):
    t = timeit('find_percentile(_a, _b, _p)',
               setup='from __main__ import find_percentile, _a, _b, _p',
               number=exec_times)
    t /= exec_times
    print(f'The algorithm worked for {t:.9f} seconds')


if __name__ == '__main__':
    run_unit_tests()
    run_stress_test()
    _a, _b, _p = get_max_test()
    run_max_test()
