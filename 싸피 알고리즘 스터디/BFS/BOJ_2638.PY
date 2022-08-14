import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    o_cheeze_q = deque()
    d_cheeze_q = deque()
    outside = [[False] * M for _ in range(N)] # 바깥쪽 공기 체크
    q.append((0, 0))
    outside[0][0] = True

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and not outside[nx][ny]: 
                if graph[nx][ny] == 1: # 치즈이면
                    o_cheeze_q.append((nx,ny)) # 바깥쪽 공기와 맞닿은 치즈큐에 추가
                else: # 바깥쪽 공기이면 
                    outside[nx][ny] = True # 공기 추가
                    q.append((nx,ny)) # 큐에 추가
    
    while o_cheeze_q: # 바깥쪽 공기와 맞닿은 치즈
        x, y = o_cheeze_q.popleft()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 바깥쪽 공기이면
            if 0<=nx<N and 0<=ny<M and graph[nx][ny] == 0 and outside[nx][ny]:
                cnt += 1 # 횟수 증가
        if cnt >= 2: # 2개 이상 면이 바깥공기와 닿았다면
            d_cheeze_q.append((x,y)) # 삭제할 치즈 큥[ 추가]
    
    while d_cheeze_q:
        x,y = d_cheeze_q.popleft() 
        graph[x][y] = 0 # 치즈 녹이기

def checkcheese():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                return True
    return False

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
hour = 0

while checkcheese(): # 한 턴 끝날때마다
    hour += 1 # 시간 추가
    bfs()
    
print(hour)

