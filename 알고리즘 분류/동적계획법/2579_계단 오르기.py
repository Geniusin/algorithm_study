import sys

input = sys.stdin.readline

num_stairs = int(input())

scores = [int(input()) for _ in range(num_stairs)]

dp = dict()

for i in range(num_stairs):

    if i == 0:
        dp[i] = scores[i]
    elif i == 1:
        dp[i] = scores[i-1] + scores[i]
    elif i == 2:
        dp[i] = max(scores[i-1], scores[i-2]) + scores[i]
    else:
        dp[i] = max(dp[i-3] + scores[i-1], dp[i-2]) + scores[i]

print(dp[num_stairs-1])
