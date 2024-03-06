import sys
input = sys.stdin.readline

N = int(input())

costs = [int(input()) for _ in range(N)]
costs.sort(reverse=True)

tmp = 0
total_cost = 0
for i in range(N):
    if tmp < 2:
        total_cost += costs[i]

        tmp += 1
    else:
        tmp = 0

print(total_cost)