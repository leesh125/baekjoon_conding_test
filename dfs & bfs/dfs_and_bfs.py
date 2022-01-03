from collections import deque


def dfs(s):
    visited[s] = True
    print(s, end=' ')

    for i in graph[s]:
        if not visited[i]:
            dfs(i)


def bfs(s):
    queue = deque([s])

    visited[s] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                

n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

visited = [False] * (n+1)

dfs(start)
print()
visited = [False] * (n+1)
bfs(start)

