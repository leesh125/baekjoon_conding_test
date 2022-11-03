import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j,standard,visited,c):
    q = deque()
    q.append((i,j))

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                if not c:
                    if graph[nx][ny] == standard:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                else:
                    if (standard == 'R' or standard == 'G') and graph[nx][ny] in ['R','G']:
                        visited[nx][ny] = True
                        q.append((nx,ny))
                    elif standard == 'B' and graph[nx][ny] == standard:
                        visited[nx][ny] = True
                        q.append((nx,ny))
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
o_visited = [[False] * N for _ in range(N)]
c_visited = [[False] * N for _ in range(N)]
cnt1, cnt2 = 0,0

for i in range(N):
    for j in range(N):
        if not o_visited[i][j]:
            o_visited[i][j] = True
            bfs(i,j,graph[i][j],o_visited,False)
            cnt1 += 1
        if not c_visited[i][j]:
            c_visited[i][j] = True
            bfs(i,j,graph[i][j],c_visited,True)
            cnt2 += 1
            
print(cnt1, cnt2)
