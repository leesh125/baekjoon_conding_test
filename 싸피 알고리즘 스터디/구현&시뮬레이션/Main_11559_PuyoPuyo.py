import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    global remove
    q = deque()
    q.append((i,j))
    visited = [[False] * 6 for _ in range(12)]
    visited[i][j] = True
    dup_visited[i][j] = True
    standard_char = graph[i][j]
    remove_list = [(i,j)]
    area = 1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<12 and 0<=ny<6 and not visited[nx][ny] and graph[nx][ny] == standard_char:
                remove_list.append((nx,ny))
                area += 1
                q.append((nx,ny))
                visited[nx][ny] = True
                dup_visited[nx][ny] = True
    if area >= 4:
        remove.extend(remove_list)

def remove_block():
    for x,y in remove:
        graph[x][y] = '.'

def down():
    stack = []
    for c in range(6):
        nr = 11
        for r in range(12):
            if graph[r][c] != '.':
                stack.append(graph[r][c])
                graph[r][c] = '.'
        while stack:
            block = stack.pop()
            graph[nr][c] = block
            nr -= 1

graph = [list(input().rstrip()) for _ in range(12)]
time = 0
#반복문
while True:
    dup_visited = [[False] * 6 for _ in range(12)]
    remove = []

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and not dup_visited[i][j]:
                bfs(i,j)
    if not remove:
        break
    else:
        remove_block()
        down()
        time += 1

print(time)