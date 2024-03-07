import sys
input = sys.stdin.readline

num_drinks = int(input())

vol_drinks = list(map(int, input().split()))
vol_drinks.sort(reverse=True)
vol = vol_drinks[0]
for drink in vol_drinks[1:]:
    vol = max((vol + (drink / 2)), (drink + (vol / 2)))


print(vol)

