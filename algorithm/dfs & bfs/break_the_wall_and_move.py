import sys, copy
from collections import deque

def bfs():
    queue = deque()
    queue.append((1,0,0)) 
    visited[1][0][0] = 1 # cnt 1이 벽을 안 부술때의 그래프

    while queue:
        cnt, x, y = queue.popleft()
        
        if x == n-1 and y == m-1:         # 마지막 도달 시 현재 cnt, x, y로 값 출력
            return visited[cnt][n-1][m-1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= n or nx < 0 or ny >= m or ny < 0: # 범위 초과
                continue

            if not visited[cnt][nx][ny]:  # 방문했던 곳 다시 방문하지 않게
                if graph[nx][ny] == 0: # 벽이 없으면 직진
                    visited[cnt][nx][ny] = visited[cnt][x][y] + 1 # 1을 추가하고
                    queue.append((cnt,nx,ny)) # 그대로 q에 추가
                if graph[nx][ny] == 1 and cnt == 1: # 벽이 있는데 cnt가 1이면(아직 안부셨다면)
                    visited[0][nx][ny] = visited[cnt][x][y] + 1 # 현재 visited 값을 cnt 0이 있는 곳으로 넘겨줌(벽을 부셨을 경우 그래프)
                    queue.append((cnt-1,nx,ny)) # cnt-1 = 0 을 통해 벽을 부셨을 때의 그래프로 이동
    return -1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
n, m = map(int, sys.stdin.readline().rstrip().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))
visited = [[[0] * m for _ in range(n)] for _ in range(2)] # 3차원 배열을 통해 벽을 부술때랑 안부술때랑 그래프를 만듦


print(bfs())
