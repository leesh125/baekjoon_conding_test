import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    q = deque()
    q.append((x,y))
    
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N :
                if ans[x][y] + graph[nx][ny] < ans[nx][ny]:
                    q.append((nx,ny))
                    ans[nx][ny] = ans[x][y] + graph[nx][ny]

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    graph = [list(map(int, input().rstrip())) for _ in range(N)]
    INF = float('inf')
    ans = [[INF for _ in range(N)] for _ in range(N)]
    ans[0][0] = 0

    bfs(0,0)
    print('#{} {}'.format(test_case, ans[N-1][N-1]))
