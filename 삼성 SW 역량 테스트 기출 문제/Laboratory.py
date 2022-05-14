import sys, copy
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)] # 방
virus = [(i,j) for i in range(n) for j in range(m) if graph[i][j] == 2] # 바이러스 좌표
visited = [[0 for _ in range(m)] for _ in range(n)] # bfs 방문 처리
dx,dy = [-1,1,0,0],[0,0,-1,1] # 상,하,좌,우 이동
coordinate = [(i,j) for i in range(n) for j in range(m) if graph[i][j] == 0] # 0인 것들의 좌표
all_combi = list(combinations(coordinate,3)) # 0인 것들의 좌표 조합(3개 묶어서)
max_zero = 0 # 그래프에서 0의 최대 cnt

# 그래프에서 0의 갯수 세기
def count_max_zero(copy_graph): 
    global max_zero
    cnt = 0
    for i in range(n):
        cnt += copy_graph[i].count(0)
    max_zero = max(max_zero, cnt) # 최댓값 갱신

# bfs 탐색
def bfs(x,y,copy_graph, copy_visited): 
    q = deque([(x,y)]) # 입력받은 바이러스 x,y 좌표를 큐에 추가
    copy_visited[x][y] = 1 # 해당 좌표 방문처리

    while q: # 큐 있을동안
        x, y = q.popleft() 

        for i in range(4): # 상하좌우 이동
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]: # 범위내에 있을떄
                if copy_graph[nx][ny] == 0: # 해당 좌표가 퍼질 수 있는 곳이라면(0이라면)
                    copy_graph[nx][ny] = 2 # 퍼뜨리기
                    copy_visited[nx][ny] = 1 # 방문 처리
                    q.append((nx,ny)) # 큐에 추가

for combi in all_combi: # 모든 벽을 세울 수 있는 그래프 조합 순회
    copy_graph = copy.deepcopy(graph) # 그래프 깊은 복사
    copy_visited = copy.deepcopy(visited) # 방문 그래프 깊은 복사

    for x,y in combi:
        copy_graph[x][y] = 1 # 벽세우기
    
    for i,j in virus: # 바이러스 x,y 좌표
        bfs(i,j,copy_graph,copy_visited) # bfs 수행

    count_max_zero(copy_graph) # 그래프의 0의 갯수 구하기

print(max_zero)
