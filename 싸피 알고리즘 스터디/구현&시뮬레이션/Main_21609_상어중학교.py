import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))
    visited = [[False] * N for _ in range(N)]
    visited[i][j] = True
    dup_visited[i][j] = True
    standard_num = graph[i][j]
    remove_list = [(i,j)]
    area = 1
    rainbow = 0

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] in [0,standard_num]:
                if graph[nx][ny] == standard_num:
                    dup_visited[nx][ny] = True  
                elif graph[nx][ny] == 0:   
                    rainbow += 1
                area += 1
                visited[nx][ny] = True
                q.append((nx,ny))
                remove_list.append((nx,ny))
    return area, rainbow, remove_list

def down():
    global graph
    for y in range(N):
        stack = []
        nr = 0
        for x in range(N):
            if graph[x][y] == -1:
                nr = x-1
                while stack:
                    num = stack.pop()
                    graph[nr][y] = num
                    nr -= 1
            elif graph[x][y] != -2:
                stack.append(graph[x][y])
                graph[x][y] = -2

        nr = N-1            
        while stack:
            num = stack.pop()
            graph[nr][y] = num
            nr -= 1

def rotate(graph):
    new_graph = [[0] * N for _ in range(N)]
    for i in range(N):
        temp = graph[i][::-1]
        for j in range(N):
            new_graph[j][i] = temp[j]
    return new_graph


N,M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
ans = 0

### 반복 시작
while True:
    dup_visited = [[False] * N for _ in range(N)]
    standard_row,standard_col = 0,0
    max_area, max_rainbow, max_remove_list = 0,0,[]
    for i in range(N):
        for j in range(N):
            if 1<=graph[i][j]<=M and not dup_visited[i][j]:
                area, rainbow, remove_list = bfs(i,j)
                if area > max_area:
                    standard_row, standard_col,max_area, max_rainbow, max_remove_list = i,j,area, rainbow, remove_list
                elif area == max_area:
                    if rainbow > max_rainbow:
                        standard_row, standard_col,max_area, max_rainbow, max_remove_list = i,j,area, rainbow, remove_list
                    elif rainbow == max_rainbow:
                        if i > standard_row:
                            standard_row, standard_col,max_area, max_rainbow, max_remove_list = i,j,area, rainbow, remove_list
                        elif i == standard_row:
                            if j > standard_col:
                                standard_row, standard_col,max_area, max_rainbow, max_remove_list = i,j,area, rainbow, remove_list

    if max_area < 2:
        break      

    for x,y in max_remove_list:
        graph[x][y] = -2

    ans += (max_area**2)

    down()
    graph = rotate(graph)
    down()
print(ans)