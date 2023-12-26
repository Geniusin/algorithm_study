from collections import deque
import sys
input = sys.stdin.readline


num_com = int(input())

num_pair = int(input())

graph = [[] for _ in range(num_com+1)]

for n in range(num_pair):

    u, v = map(int, input().split())

    graph[u].append(v)
    graph[v].append(u)


visited = [False] * (num_com + 1)
def bfs(graph, start, visited):

    queue = deque()

    queue.append(graph[start])
    visited[start] = True
    while queue:
        v = queue.popleft()

        for i in v:
            if not visited[i]:
                bfs(graph, i, visited)

bfs(graph, 1, visited)

print(sum(visited)-1)