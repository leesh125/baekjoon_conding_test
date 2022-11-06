import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(n,i,j,visited):
    q = deque()
    q.append((i,j))
    visited[i][j] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] > n:
                q.append((nx,ny))
                visited[nx][ny] = True

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(1,101):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for x in range(N):
        for y in range(N):
            if not visited[x][y] and graph[x][y] > i:
                bfs(i,x,y,visited)
                cnt += 1
    ans = max(ans,cnt)
print(ans if ans != 0 else 1)