z = [1, 1, 1, 2, 2, 3, 4, 5, 7]

n = 10
# 재귀
def tri(n):

    if n == 1: return 1
    if n == 2: return 1
    if n == 3: return 1
    if n == 4: return 2
    if n == 5: return 2
    else:
        return tri(n-1) + tri(n-5)


print(tri(5))

n = 12
mem = [-1 for _ in range(n+1)]
def tri_dp(n):

    if n == 1: return 1
    if n == 2: return 1
    if n == 3: return 1
    if n == 4: return 2
    if n == 5: return 2

    if mem[n] != -1:
        return mem[n]
    mem[n] = tri(n-1) + tri(n-5)

    return mem[n]

print(tri_dp(n))