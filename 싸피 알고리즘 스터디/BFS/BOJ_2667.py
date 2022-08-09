from collections import deque
import sys
input = sys.stdin.readline

dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    graph[i][j] = 0
    total = 1

    while q:
        x,y = q.popleft()
        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 1:
                total += 1
                graph[nx][ny] = 2
                q.append((nx,ny))
    
    return total

N = int(input())
graph = [list(map(int,input().rstrip())) for _ in range(N)]
ans = []

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            ans.append(bfs(i,j))
            
            
print(len(ans))
for a in sorted(ans): print(a)