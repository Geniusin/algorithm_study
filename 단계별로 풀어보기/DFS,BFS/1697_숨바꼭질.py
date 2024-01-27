import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

if N >= K:
    print(N-K)
else:


    queue = deque([N])

    visited = [0] * 100001
    while queue:
        x = queue.popleft()

        if x == K:
            break

        for i in (x -1, x+1, x*2):
            if (0 <= i <= 100000) and (not visited[i]):
                visited[i] = visited[x] + 1
                queue.append(i)
    print(visited[K])