# 12865 평범한배낭

# Combinations를 활용한 완전탐색 풀이
import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())

best_value = 0
weights = []
values = []
for n in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

itrs = [i for i in range(N)]


# 1개씩
for i in range(N):
    combs = combinations(itrs, i)

    for ids in combs:
        tmp_w = 0
        tmp_v = 0
        for id in ids:
            tmp_w += weights[id]
            tmp_v += values[id]
        if (tmp_w <= K) and (tmp_v >= best_value):

            best_value = tmp_v
print(best_value)

K = 6
N = 6
dp_table =[[0 for _ in range(N+1)] for _ in range(K+1)]



# 피보나치


def fibonacci(num):

    if num == 0:
        return 0
    elif num == 1:
        return 1

    if dps[num] != 0:
        return dps[num]
    dps[num] = fibonacci(num-1) + fibonacci(num-2)

    return dps[num]



T = int(input())
for t in range(T):
    n = int(input())
    dps = [[0, 0] for _ in range(41)]


    dps[1] = [1, 0]
    dps[2] = [0, 1]
    dps[3] = [1, 1]

    if n<= 3:
        print(dps[n][0], dps[n][1])

    else:
        for i in range(4, n+1):
            dps[i] = [dps[i-1][0]+dps[i-2][0], dps[i-1][1]+dps[i-2][i]]

