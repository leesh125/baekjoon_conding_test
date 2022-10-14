import sys
from collections import deque
input = sys.stdin.readline
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]

def check_cloud():
    for i in range(N):
        for j in range(N):
            if graph[i][j] >= 2 and not cloud_visited[i][j]:
                graph[i][j] -= 2
                q.append((i,j))

N,M = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
magics = [list(map(int,input().split())) for _ in range(M)]
ans = 0
cloud_visited = [[False] * N for _ in range(N)]
clouds = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]
q = deque(clouds)

for magic in magics:
    dir, moveCnt = magic
    dir -= 1
    for g in graph:
        print(g)    
    print()
    print(q)
    for i in range(len(q)):
        x,y = q.popleft()
        nx = (x + dx[dir] * moveCnt) % N
        ny = (y + dy[dir] * moveCnt) % N
        q.append((nx,ny))
    print(q)
    while q: # 4번 조건 까지 
        cloudX,cloudY = q.popleft()
        graph[cloudX][cloudY] += 1
        cloud_visited[cloudX][cloudY] = True

        for i in [1,3,5,7]:
            dig_x = cloudX + dx[i]
            dig_y = cloudY + dy[i]

            if 0<=dig_x<N and 0<=dig_y<N and graph[dig_x][dig_y] > 0:
                graph[cloudX][cloudY] += 1
    for g in graph:
        print(g)    
    print()
    check_cloud()
    for g in graph:
        print(g)    
    print()

for g in graph:
    ans += sum(g)
print(ans)

