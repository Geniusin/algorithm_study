import sys
input = sys.stdin.readline

X = int(input())
dp = {
    0: 0,
    1: 0,
}

def make_1(num):

    if num in dp.keys():
        return dp[num]

    if num % 6 == 0:
        dp[num] = min(make_1(num//3), make_1(num//2)) + 1

    elif num % 3 == 0:
        dp[num] = min(make_1(num//3), make_1(num-1)) + 1

    elif num % 2 == 0:
        dp[num] = min(make_1(num//2), make_1(num-1)) + 1

    else:
        dp[num] = make_1(num-1) + 1

    return dp[num]

print(make_1(X))

