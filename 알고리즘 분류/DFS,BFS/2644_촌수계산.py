import sys
from collections import deque


input = sys.stdin.readline


N = int(input())

X, Y = map(int, input().split())

M = int(input())

graphs = [[] for _ in range(N+1)]
for m in range(M):
    u, v = map(int, input().split())

    graphs[u].append(v)
    graphs[v].append(u)

for gph in graphs:
    gph.sort(reverse=False)


visited = [False] * (N+1)

res = []
def dfs(graph, start, visit, goal, d):
    visit[start] = True

    d += 1
    if start == goal:
        res.append(d)
    for i in graph[start]:

        if visit[i] == False:

            dfs(graph, i, visit, goal, d)


dfs(graphs, X, visited, Y, 0)

if len(res) == 0:
    print(-1)
else:
    print(res[0]-1)

