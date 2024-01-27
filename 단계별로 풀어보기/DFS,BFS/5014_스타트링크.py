import sys
from collections import deque


input = sys.stdin.readline

F, S, G, U, D = map(int, input().split())


q = deque([S])
visited = [0] * 1000001

visited[S] = 1 # 이거떄문에 맞음 반례 2 2 1 0 1
while q:

    x = q.popleft()

    if x == G:
        break
    for i in (x-D, x+U):
        if 1 <= i <= F and not visited[i]:
            visited[i] = visited[x] + 1

            q.append(i)
if S == G:
    print(visited[G]-1)
elif visited[G] == 0:
    print('use the stairs')
else:
    print(visited[G]-1)
