import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

path = []
def dfs(graph, v, visited):

    visited[v] = True
    path.append(v)
    for i in graph[v]:

        if not visited[i]:

            dfs(graph, i, visited)
    return


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]

for m in range(M):
    u, v = list(map(int, input().split()))
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort(reverse=True)

visited = [False] * (N+1)
dfs(graph, R, visited)

result = [0]*(N+1)
for idx, node in zip(range(1, len(path) + 1), path):
    result[node] = idx

print(*result[1:], sep="\n")