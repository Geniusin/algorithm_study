x = [-1 for _ in range(30)]


def bridge(n, m):

    if n == m: return 1
    if n == 1: return m

    if x[n] != -1:
        return x[n]

    x[n] = bridge(1, m-n+1) + bridge(n-1, m-1)
    return x[n]

print(bridge(13, 29))

