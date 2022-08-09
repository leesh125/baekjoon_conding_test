import sys
from collections import deque
input = sys.stdin.readline

dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]

def bfs(x,y,visited):
    visited[x][y] = True
    while q:
        x,y,cnt = q.popleft()

        if x == def_x and y == def_y:
                return cnt

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append([nx,ny,cnt+1])

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    now_x, now_y = map(int,input().split())
    def_x, def_y = map(int,input().split())
    visited = [[False] * N for _ in range(N)]
    cnt = 0

    q = deque()
    q.append([now_x,now_y,cnt])
    print(bfs(now_x,now_y,visited))
