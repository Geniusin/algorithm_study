import sys
input = sys.stdin.readline

num_coins, value_coins = map(int, input().split())

coins = [int(input()) for _ in range(num_coins)]


cnt_coins = 0
for coin in coins[::-1]:

    n = value_coins // coin
    k = value_coins % coin

    if n <= 0:
        continue
    else:
        cnt_coins += n
        value_coins = k

print(cnt_coins)