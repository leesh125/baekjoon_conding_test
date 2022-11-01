import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def firemove():
    for i in range(len(fireq)):
        x,y = fireq.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < R and 0 <= ny < C and graph[nx][ny] == '.' and not fire_visited[nx][ny]:
                graph[nx][ny] = 'F'
                fire_visited[nx][ny] = True
                fireq.append((nx,ny))

def bfs(jihoon):
    global ans
    q = deque()
    visited = [[False] * C for _ in range(R)]
    q.append((jihoon[0],jihoon[1],0))
    visited[jihoon[0]][jihoon[1]] = True

    while q:
        for i in range(len(q)):
            x,y,cnt = q.popleft()

            if graph[x][y] == 'F': continue

            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]

                if 0 > nx or nx >= R or 0 > ny or ny >= C:
                    ans = cnt + 1
                    return True
                if graph[nx][ny] == '.' and not visited[nx][ny]:
                    q.append((nx,ny,cnt+1))
                    visited[nx][ny] = True
        firemove()
    return False

R,C = map(int, input().split())
graph = []
jihoon = []
fireq = deque()
ans = 0
fire_visited = [[False] * C for _ in range(R)]

for i in range(R):
    temp = list(input().rstrip())
    graph.append(temp)
    for j in range(C):
        if graph[i][j] == 'J':
            jihoon = [i,j]
        elif graph[i][j] == 'F':
            fireq.append((i,j))
            fire_visited[i][j] = True
if(bfs(jihoon)): print(ans)
else: print('IMPOSSIBLE')