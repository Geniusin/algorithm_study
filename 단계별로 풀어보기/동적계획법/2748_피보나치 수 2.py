
N = int(input())
mem = [-1 for _ in range(N+1)]
def fbn(n):

    if n == 0: return 0
    if n == 1: return 1

    if mem[n] != -1:
        return mem[n]
    mem[n] = fbn(n-1) + fbn(n-2)

    return mem[n]

print(fbn(N))
