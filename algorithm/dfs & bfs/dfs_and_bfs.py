from collections import deque

# dfs 탐색 - 더이상 방문할게 없을 때 까지 깊이
def dfs(s): 
    visited[s] = True
    print(s, end=' ')

    for i in graph[s]:
        if not visited[i]:
            dfs(i)

# bfs 탐색 - 인접노드가 더이상 방문할 게 없을 때 까지
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

graph = [[] for _ in range(n + 1)] # 보통 그래프는 1부터 시작하기에 1늘려준 이차원 배열 생성
for _ in range(m): 
    x, y = map(int, input().split()) # 한줄 씩 입력 받아
    graph[x].append(y) # (ex. 1 2) 1 노드는 2 노드 방문
    graph[y].append(x) # 2 노드는 1 방문

for i in graph: 
    i.sort() # 노드의 방문을 정렬 해준다

visited = [False] * (n+1) # 노드의 방문을 체크하기 위한 visited 배열

dfs(start)
print()
visited = [False] * (n+1)
bfs(start)

