self_num = list(range(1, 10000))
nums = list(range(1, 10000))


for X in range(1, 10000):
    N = X
    while N < 10000:
        if N < 10:
            N = N + N
            if N in self_num:
                self_num.remove(N)

        elif N < 100:
            N = N + N//10 + N%10
            if N in self_num:
                self_num.remove(N)

        elif N < 1000:
            N = N + N//100 + N//10 + N%10
            if N in self_num:
                self_num.remove(N)

        elif N < 10000:
            N = N + N//1000 + N // 100 + N//10 + N%10
            if N in self_num:
                self_num.remove(N)

