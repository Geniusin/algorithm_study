import sys
from collections import deque
input=sys.stdin.readline


path_bfs = []
def bfs(graph, start, visited):

    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        path_bfs.append(str(v))
        # print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True



path_dfs = []
def dfs(graph, start, visited):

    visited[start] = True
    path_dfs.append(str(start))
    # print(start, end=' ')
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)


N, M, V = map(int, input().split())

visited_bfs = [False] * (N+1)
visited_dfs = [False] * (N+1)

graph = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort(reverse=False)


dfs(graph, V, visited_dfs)
bfs(graph, V, visited_bfs)

print(" ".join(path_dfs))
print(" ".join(path_bfs))
