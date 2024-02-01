# 1463_1로 만들기
# BFS 풀이 -> DP top-down, bottom-up 방식으로도 풀어볼 것
import sys
from collections import deque

input = sys.stdin.readline

X = int(input())
cnt = 0

visited = [0] * (X+1)
q = deque([X])
visited[X] = 1

while q:

    num = q.popleft()
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


