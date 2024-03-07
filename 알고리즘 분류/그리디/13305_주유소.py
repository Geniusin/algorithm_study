import sys
input = sys.stdin.readline

num_cities = int(input())

len_cities = list(map(int, input().split()))

cost_oil = list(map(int, input().split()))[:-1]


least_cost = cost_oil[0] * len_cities[0]
tmp_cost = cost_oil[0]
for cost, length in zip(cost_oil[1:], len_cities[1:]):

    if cost < tmp_cost:
        tmp_cost = cost
        least_cost += tmp_cost * length
    else:
        least_cost += tmp_cost * length


print(least_cost)