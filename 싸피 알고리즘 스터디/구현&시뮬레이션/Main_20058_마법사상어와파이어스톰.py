import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def rotate(sep_graph,l):
    new_graph = [[0] * l for _ in range(l)]
    for row in range(l-1,-1,-1):
        for col in range(l):
            new_graph[col][row] = sep_graph[l-1-row][col]
    return new_graph

def melt():
    melt_list = []
    for x in range(N):
        for y in range(N):
            if graph[x][y] == 0: continue
            cnt = 0
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] >= 1:
                    cnt += 1
            if cnt < 3:
                melt_list.append((x,y))
    return melt_list

def bfs(x,y):
    q = deque()
    q.append((x,y))
    max_cnt = 1
    visited[x][y] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] >= 1:
                visited[nx][ny] = True
                max_cnt += 1
                q.append((nx,ny))
    return max_cnt

N, Q = map(int,input().split())
N = 2 ** N
graph = [list(map(int,input().split())) for _ in range(N)]
magics = list(map(int,input().split()))
visited = [[False] * N for _ in range(N)]
total, mass_total = 0,0

for L in magics:
    L = 2 ** L
    new_graph = [[0] * N for _ in range(N)]
    if L == 1:
        pass
    else:
        for i in range(0,N,L):
            for j in range(0,N,L):
                temp_graph = []
                for x in range(i,i+L):
                    temp_graph.append(graph[x][j:j+L])

                r_graph = rotate(temp_graph,L)

                for x in range(i,i+L):
                    graph[x][j:j+L] = r_graph[x-i]

    melt_list = melt()
    if melt_list:
        for x,y in melt_list:
            graph[x][y] -= 1

for g in graph:
    total += sum(g)
print(total)

for x in range(N):
    for y in range(N):
        if graph[x][y] != 0 and not visited[x][y]:
            mass_total = max(mass_total,bfs(x,y))
print(mass_total)