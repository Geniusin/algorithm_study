import sys

input = sys.stdin.readline

N, K = map(int, input().split())
DP =[[0 for _ in range(N+1)] for _ in range(K+1)]


weights = []
values = []
for n in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)


for i in range(1, len(weights)+1):
    w = weights[i-1]
    v = values[i-1]

    for k in range(0, len(DP)):

        if k < w:
            DP[k][i] = DP[k][i-1]
        else:
            DP[k][i] = max(DP[k][i-1], DP[k-w][i-1]+v)


print(DP[K][N-1])


# Combinations를 활용한 완전탐색 풀이 (당연히 시간초과)
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