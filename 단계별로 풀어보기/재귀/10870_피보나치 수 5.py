N = int(input())

def pibonachi(n):

    if n == 0: return 0
    if n == 1: return 1

    for i in range(n):
        return pibonachi(n-2) + pibonachi(n-1)

print(pibonachi(N))