import sys
from collections import deque

# bfs 함수
def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft() # 방문 했던 것은 pop하고 x,y에 담아주기

        for i in range(4): # 상하좌우
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= k: # 범위 벗어날 경우
                continue
            if graph[nx][ny] == 0:  # 이동할 수 없는 칸
                continue
            if graph[nx][ny] == 1:  # 길이 있다면
                graph[nx][ny] = graph[x][y] + 1 # 해당 길 +1 해서 이동 수를 기록
                queue.append((nx,ny)) # 끝이 날때까지 큐에 계속 추가
        
    return graph[n-1][k-1] # 마지막 칸에 있는 이동 수 반환


n, k = map(int, sys.stdin.readline().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))