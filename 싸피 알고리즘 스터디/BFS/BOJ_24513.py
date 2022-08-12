import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    q.append((virus1_x,virus1_y,1))
    q.append((virus2_x,virus2_y,2))
    visited[virus1_x][virus1_y], visited[virus2_x][virus2_y] = True, True

    while q:
        x,y,virus = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny] != -1:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    graph[nx][ny] = virus
                    q.append((nx,ny,virus))
                

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus1_x, virus1_y,virus2_x, virus2_y = 0, 0, 0, 0 
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            virus1_x = i; virus1_y = j
        elif graph[i][j] == 2:
            virus2_x = i; virus2_y = j

