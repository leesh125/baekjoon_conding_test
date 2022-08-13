import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    q = deque()
    origin_count = 1 # 이동 횟수 cnt
    q.append((virus1_x,virus1_y,1,origin_count))
    q.append((virus2_x,virus2_y,2,origin_count))
    visited[virus1_x][virus1_y], visited[virus2_x][virus2_y] = True, True

    while q:
        x,y,virus,count = q.popleft()
        if ban[x][y]: continue # 밴 당한 곳 패스(3바이러스면 더이상 확장 필요 x)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M and graph[nx][ny] != -1:
                if not visited[nx][ny]: # 방문하지 않은곳이라면
                    if graph[nx][ny] == 0: # 바이러스가 없는 곳이면 퍼트리기
                        visited[nx][ny] = True
                        count_list[nx][ny] = count
                        graph[nx][ny] = virus
                        q.append((nx,ny,virus,count+1))
                else: # 방문한 곳일 때
                    # 3번 바이러스의 조건이 맞으면
                    if ((virus == 1 and graph[nx][ny] == 2) or (virus == 2 and graph[nx][ny] == 1)) and count_list[nx][ny] == count:
                        graph[nx][ny] = 3 # 3번 바이러스
                        ban[nx][ny] = True # 밴 때리기
                    
N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
virus1_x, virus1_y,virus2_x, virus2_y = 0, 0, 0, 0 
visited = [[False] * M for _ in range(N)]
ban = [[False] * M for _ in range(N)]
count_list = [[0] * M for _ in range(N)]
virus_cnt2 = [0,0,0,0]

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            virus1_x = i; virus1_y = j
        elif graph[i][j] == 2:
            virus2_x = i; virus2_y = j
bfs()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            virus_cnt2[1] += 1
        elif graph[i][j] == 2:
            virus_cnt2[2] += 1
        elif graph[i][j] == 3:
            virus_cnt2[3] += 1
print(*virus_cnt2[1:])