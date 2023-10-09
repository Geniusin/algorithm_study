def fast_sum(n):
    if n == 1: return 1
    if n%2 == 1: return n + fast_sum(n-1)

    return 2 * fast_sum(n/2) + (n/2)**2


print(fast_sum(10))

import sys

input = sys.stdin.readline

S = input()[:-1]

alpha_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=',
              'a', 'b', 'd' 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'o', 'p', 'q', 'r', 't', 'u', 'v', 'w', 'x', 'y']
cnt = 0
for alpha in alpha_list:
    while True:
        n = S.find(alpha)
        if n != -1:
            if n == 0:
                S = S[len(alpha):]
            else:
                a = S[0: n]
                b = S[n+len(alpha):]
                S = a + b
            cnt += 1

        else:
            break
