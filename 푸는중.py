# 12865 평범한배낭
import re
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

##

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
def solution(N, stages):
    answer = []
    res = []
    rail_rat = 0
    for n in range(1, N + 1):
        reached = sum([1 for s in stages if s <= n])
        not_clear = sum([1 for s in stages if s == n])

        if reached == 0:
            rail_rat = 0
        else:
            fail_rat = not_clear / reached
        res.append(fail_rat)
    for n in range(N):
        answer.append(res.index(max(res)))
    return answer


print(solution(N, stages))


x = [0.125, 0.42857142857142855, 0.5, 0.5, 0.0]
y = sorted(x, reverse=True)
ans = []
for i in range(len(x)):
    rank = x.index(y[i])

    ans.append(x.index(y[i])+1)
    x[rank] = -1

x = "Hel+lo world!"
tmp = []
x = x.lower()

for i in range(len(x)-1):
    word = x[i:i+2]
    p = re.search('[a-z]+', word).group()
    if len(p) == 2:
        tmp.append(x[i:i+2])

re.match('\w', x)