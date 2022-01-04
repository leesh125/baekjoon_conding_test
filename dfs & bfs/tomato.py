import sys
from collections import deque

def bfs():
    queue = deque()
    for x,y in e_arr: # 썪은 토마토가 하나가 아니라 다른곳에도 있을 수 있기에, 동시에 썩기 시작하게
        queue.append((x,y))
        
    global max_num # 다 썩는데 걸리는 시간

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m: # 범위 벗어날 떄
                continue

            if graph[nx][ny] == -1: # 없는 칸이면
                continue

            if graph[nx][ny] == 0: # 이웃해 있는 싱싱한 토마토라면
                graph[nx][ny] = graph[x][y] + 1 # 썩기 시작(+1)
                if max_num < graph[nx][ny]: # 가장 높은 수가 결국 전체 토마토가 썩는데 걸리는 시간
                    max_num = graph[nx][ny]
                queue.append((nx, ny))
       
            


m, n = map(int, sys.stdin.readline().split())
graph = [list(map(int, input().split())) for i in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

e_arr = []
max_num = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: # 썩은 토마토 처음부터 찾기
            e_arr.append([i,j])

bfs() # bfs 스행

# 결과에 따라 출력이 다르게끔 하는 함수
def true_false():
    
    not_zero = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0: # 하나라도 안 썩은게 있으면 -1 리턴
                return -1
            if graph[i][j] == -1 or graph[i][j] == 1: # 처음부터 썩힐게 없는 토마토 판이라면 
                not_zero += 1
    
    if not_zero == m * n: # 전체 토마토 갯수랑 비교하기
        return 0
    else:
        return max_num-1 # 전체 썩는데 걸린 시간 (-1 이유: 처음을 0일이 아닌 1일 부터 시작했음)

    

print(true_false())