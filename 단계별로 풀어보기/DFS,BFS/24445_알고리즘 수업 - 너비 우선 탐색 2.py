import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

path = []
def bfs(graph, start, visited):

    queue = deque([start])

    visited[start] = True
    path.append(start)
    while queue:

        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                path.append(i)
N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for m in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)

visited = [False] * (N+1)
bfs(graph, R, visited)

result = [0]*(N+1)
for idx, node in zip(range(1, len(path) + 1), path):
    result[node] = idx

print(*result[1:], sep="\n")