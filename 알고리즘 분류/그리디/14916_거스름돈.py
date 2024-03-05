import sys
input = sys.stdin.readline

cost = int(input())


cnt_coin_5 = cost // 5
cnt_coin_2 = (cost % 5) // 2


if (cost % 5) % 2 == 0:
    pass
else:
    cnt_coin_5 -= 1
    cnt_coin_2 = ((cost % 5) + 5) // 2

if cnt_coin_5 == -1:
    print(-1)
else:
    print(cnt_coin_2 + cnt_coin_5)


# DP 풀이법
import sys
input = sys.stdin.readline

cost = int(input())

dp = [10000] * (cost+1)

for i in range(1, cost+1):
    if i == 1:
        dp[i] = 1000000
    elif i == 2:
        dp[i] = 1
    elif i == 3:
        dp[i] = 1000000
    elif i == 4:
        dp[i] = 2
    elif i == 5:
        dp[i] = 1
    else:
        dp[i] = min(dp[i-2]+1, dp[i-5]+1)

if dp[cost] == 1000000:
    print(-1)
else:
    print(dp[cost])