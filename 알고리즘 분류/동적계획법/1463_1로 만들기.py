# 1463_1로 만들기
# BFS 풀이 -> DP top-down, bottom-up 방식으로도 풀어볼 것
import sys
from collections import deque

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

# DP- TOp-dowm
import sys
input = sys.stdin.readline

X = int(input())

dp = [-1] * (X+1)

dp[0] = 0
dp[1] = 0


def make_1(num):
    if dp[num] != -1:
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

#BFS
input = sys.stdin.readline

X = int(input())
cnt = 0

visited = [0] * (X+1)
q = deque([X])
visited[X] = 1

while q:

    num = q.popleft()
    print(num)
    if num == 1:
        break

    if num % 3 == 0:
        if visited[num//3] == 0:
            visited[num//3] = visited[num] + 1
        else:
            visited[num//3] = min(visited[num//3], visited[num] + 1)
        if num//3 not in q:
            q.append(num // 3)

    if num % 2 == 0:
        if visited[num//2] == 0:
            visited[num//2] = visited[num] + 1
        else:
            visited[num//2] = min(visited[num//2], visited[num] + 1)
        if num//2 not in q:
            q.append(num//2)

    if visited[num - 1] == 0:
        visited[num - 1] = visited[num] + 1
    else:
        visited[num - 1] = min(visited[num - 1], visited[num] + 1)
    if num-1 not in q:
        q.append(num - 1)
print(visited[1] - 1)


