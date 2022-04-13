import math


def find_percentile(a, b, p):

    #  Initialization part
    n, m = len(a), len(b)  # size of arrays
    if n > m:
        a, b, n, m = b, a, m, n  # b - biggest array, otherwise - swap
    i_min, i_max = 0, n  # pointer i lower/upper boundary
    percentile_idx = math.ceil(((m + n) * p) / 100)
    if n > 10**6 or m > 10**6 or m == 0:  # check array size conditions and at least one array is not empty
        raise ValueError

    # pointer i splits array a, pointer j splits array b
    # each of those splits give us values that fill left side of array c splitted by percentile
    # we need only maximum of these values, which will be the maxmim element of c before split
    while i_min <= i_max:
        i = (i_min + i_max) // 2
        j = percentile_idx - i
        if i < n and b[j - 1] > a[i]:  # i is small => increase
            i_min = i + 1
        elif i > 0 and a[i - 1] > b[j]:  # i is big => decrease
            i_max = i - 1
        else:  # found best split
            if i == 0:  # a is empty or all values we need in b
                left_max = b[j - 1]
            elif j == 0:  # b is empty or all values we need in a
                left_max = a[i - 1]
            else:  # biggest value of left parts of splits of a and b
                left_max = max(a[i - 1], b[j - 1])

            return f'Left_max = {left_max}, {p}-percentile(ind={percentile_idx}) = {sorted(a+b)[percentile_idx]}    {sorted(a+b)}'


if __name__ == "__main__":
    test_a, test_b, test_p = [1, 2, 7, 8, 10], [6, 12], 50
    # should print 7
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [1, 2, 7, 8], [6, 12], 50
    # should print 6
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [15, 20, 35, 40, 50], [], 30
    # should print 20
    print(find_percentile(test_a, test_b, test_p))

    test_a, test_b, test_p = [15, 20], [25, 40, 50], 40
    # should print 20
    print(find_percentile(test_a, test_b, test_p))