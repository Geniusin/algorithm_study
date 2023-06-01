
N = int(input())
mem = [-1 for _ in range(N+1)]

cnt_dp = 0
cnt_rg = 0

def fbn(n):
    global cnt_dp

    if (n == 1 or n == 2):

        return 1
    if mem[n] != -1:
        return mem[n]
    cnt_dp += 1
    mem[n] = fbn(n-1) + fbn(n-2)

    return mem[n]

def fibonachi(n):
    global cnt_rg

    if (n == 1 or n == 2):
        cnt_rg += 1
        return 1
    else:

        return fibonachi(n-2) + fibonachi(n-1)


fibonachi(N)
fbn(N)

print(cnt_rg, cnt_dp)
