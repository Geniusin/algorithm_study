import sys
# DP - Bottom-up
input = sys.stdin.readline

X = int(input())

dp = [0] * (X+1)

for i in range(2, X+1):
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[X])

seq = []
seq.append(X)
while True:
    if X <= 1:
        break

    if X % 6 == 0:
        if dp[X//3] <= dp[X//2]:
            X = X//3
            seq.append(X)
        else:
            X = X//2
            seq.append(X)

    elif X % 3 == 0:
        if dp[X//3] <= dp[X-1]:
            X = X//3
            seq.append(X)
        else:
            X -= 1
            seq.append(X)

    elif X % 2 == 0:
        if dp[X//2] <= dp[X-1]:
            X = X//2
            seq.append(X)
        else:
            X -= 1
            seq.append(X)
    else:
        X -= 1
        seq.append(X)

for i in seq:
    print(i, end=' ')