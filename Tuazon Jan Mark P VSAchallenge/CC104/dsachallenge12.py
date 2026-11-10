def bs(a, x):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        m = (lo + hi) // 2
        if a[m] == x: lo = hi = m
        if a[m] < x: lo = m + 1
        else: hi = m - 1
        return -1
    print(bs([1, 4, 6, 8, 10], 8))