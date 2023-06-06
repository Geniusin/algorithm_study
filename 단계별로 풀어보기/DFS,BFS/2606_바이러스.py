# dfs 풀이
import sys

input = sys.stdin.readline


N = int(input())
M = int(input())

graphs = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())

    graphs[u].append(v)
    graphs[v].append(u)

for gph in graphs:
    gph.sort(reverse=False)

visited = [False] *(N+1)
path = []
def dfs(graph, start, visited):

    visited[start] = True
    path.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graphs, 1, visited)

print(sum(visited)-1)

# bfs 풀이


from collections import deque


def bfs(graph, start, visited):
    queue = deque[(start)]

    while queue:

        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True