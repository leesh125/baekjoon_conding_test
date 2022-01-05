import sys
from collections import deque

def bfs():
    while queue:
        a, b, c = queue.popleft()

        for r in range(6):
            nh = a + dh[r]
            nx = b + dx[r]
            ny = c + dy[r]
            if 0<=nh<h and 0<=nx<n and 0<=ny<m and graph[nh][nx][ny] == 0: # 범위를 벗어나지 않고, 썩지않은 토마토이면
                queue.append([nh,nx,ny]) # 큐에 삽입
                graph[nh][nx][ny] = graph[a][b][c] + 1 # 썩은거로 간주
       


m, n, h = map(int, sys.stdin.readline().split())
graph = [[list(map(int, sys.stdin.readline().split())) for i in range(n)] for j in range(h)]

dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dh = [0,0,0,0,-1,1] # z축 추가(위, 아래)

queue = deque()

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 1: # 썩은 토마토 처음부터 찾기
                queue.append([k,i,j]) # 바로 큐에 삽입

bfs() # bfs 수행
max_num = 0

for k in range(h):
    for i in range(n):
        for j in range(m):
            if graph[k][i][j] == 0: # 하나라도 안 썩은게 있으면 -1 리턴
                print(-1)
                exit()
            if max_num < graph[k][i][j]: # 최댓값 비교
                max_num = graph[k][i][j]
print(max_num-1) # 전체 썩는데 걸린 시간 (-1 이유: 처음을 0일이 아닌 1일 부터 시작했음)
