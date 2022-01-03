from collections import deque

# bfs 탐색
def bfs(v):
    queue = deque([v])
    visited[v] = True
    cnt = 0
    while(queue):
        v = queue.popleft()
        
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return cnt-1 # 본인 노드도 방문한 것으로 간주되기 때문

com = int(input())
pair_num = int(input())

graph = [[] for i in range(com+1)]

for _ in range(pair_num):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for e in graph:
    e.sort()

visited = [False] * (com+1)

print(bfs(1))