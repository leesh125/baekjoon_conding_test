from collections import deque

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# def dfs(x,y,room):
#     visited = [[False] * N for _ in range(N)]
#     visited[x][y] = True
#     room = graph[x][y]    

def bfs(startX,startY):
    ans = 1
    q = deque()
    q.append((startX,startY))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and graph[nx][ny] - graph[x][y] == 1:
                ans += 1
                q.append((nx,ny))
    return ans

for tc in range(1,T+1):
    N = int(input())
    graph = [list(map(int, input().split())) for _ in range(N)]
    res = -1; max_room = int(1e9)
    for i in range(N):
        for j in range(N):
            temp = bfs(i,j)
            if temp > res:
                res = temp
                max_room = graph[i][j]
            elif temp == res:
                max_room = min(max_room, graph[i][j])

    print('#{0} {1} {2}'.format(tc, max_room, res))