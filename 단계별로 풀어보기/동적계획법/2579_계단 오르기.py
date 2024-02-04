import sys

input = sys.stdin.readline

num = int(input())

scores = []
for i in range(1, num+1):
    scores.append(int(input()))

dp = dict()

step = 0
for i in range(0, num):

    if i == 0:


    if dp[i-1] >= dp[i-2] and step < 2:
        step += 1

        dp[i] = dp[i-1] + scores[i]
    elif dp[i-1] < dp[i-2] or step >= 2:

        dp[i] = dp[i - 1] + scores[i]

        step = 0
print(dp[num-1])