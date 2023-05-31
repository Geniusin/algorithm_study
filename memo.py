def fast_sum(n):
    if n == 1: return 1
    if n%2 == 1: return n + fast_sum(n-1)

    return 2 * fast_sum(n/2) + (n/2)**2


print(fast_sum(10))