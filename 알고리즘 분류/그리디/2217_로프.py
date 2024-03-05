import sys
input = sys.stdin.readline


N = int(input())

result = -1
weights = [int(input()) for n in range(N)]
weights.sort()

best_w = sum(weights) / len(weights)

min_weights = weights[0]
if best_w > min_weights:
    result = min_weights * len(weights)

for i in range(1, len(weights)+1):

    best_w =  i * weights[-i]

    result = max(result, i * weights[-i])


print(result)