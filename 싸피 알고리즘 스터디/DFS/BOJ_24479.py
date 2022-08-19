import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):
    global order
    for g in graph[start]:
        if not visited[g]:
            visited[g] = True
            ans[g] = order
            order += 1
            dfs(g)

        

N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)
ans = [0] * (N+1)
order = 1

for _ in range(M):
    fr, to = map(int,input().split())
    graph[fr].append(to)
    graph[to].append(fr)
for i in range(1, N+1):
    graph[i] = sorted(graph[i])

ans[start] = order
order += 1
visited[start] = True
dfs(start)
for a in ans[1:]:
    print(a)