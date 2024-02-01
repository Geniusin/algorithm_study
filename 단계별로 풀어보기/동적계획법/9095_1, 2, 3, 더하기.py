# 9095_1, 2, 3 더하기

import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    X = int(input())

    dp = [0] * (X+1)


    for i in range(1, X+1):

        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] = 2
        elif i == 3:
            dp[i] = 4
        elif i == 4:
            dp[i] = 7

        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

    print(dp[X])