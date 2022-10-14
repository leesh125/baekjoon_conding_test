import sys
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def my_smell():
    for shark in shark_dir_dic:
        x,y = shark_dir_dic[shark]
        smell_graph[x][y] = [shark,K]

def move_shark():
    for shark in shark_dir_dic:
        x, y = shark_dir_dic[shark]
        temp_shark = shark - 1
        now_dir = now_shark_dir[temp_shark]

        for dir in shark_dir[temp_shark][now_dir]:
            nx = x + dx[dir]
            ny = y + dy[dir]

            if 0 <= nx < N and 0 <= ny < N and smell_graph[nx][ny] == []:
                graph[x][y] = []
                graph[nx][ny].append(shark)
                shark_dir_dic[shark] = [nx,ny]
                now_shark_dir[temp_shark] = dir
                break
        else:
            for dir in shark_dir[temp_shark][now_dir]:
                nx = x + dx[dir]
                ny = y + dy[dir]

                if 0 <= nx < N and 0 <= ny < N and smell_graph[nx][ny][0] == shark:
                    graph[x][y] = []
                    graph[nx][ny].append(shark)
                    shark_dir_dic[shark] = [nx, ny]
                    now_shark_dir[temp_shark] = dir
                    break

def remove_shark():
    for i in range(N):
        for j in range(N):
            if len(graph[i][j]) >= 2:
                shark = min(graph[i][j])
                for s in graph[i][j]:
                    if shark == s:
                        continue
                    del shark_dir_dic[s]
                graph[i][j] = [shark]
                shark_dir_dic[shark] = [i,j]

def remove_smell():
    for i in range(N):
        for j in range(N):
            if smell_graph[i][j] != []:
                shark, k = smell_graph[i][j]
                if k == 1:
                    smell_graph[i][j] = []
                else:
                    smell_graph[i][j] = [shark,k-1]

def check_shark1():
    shark1 = 0
    shark_other = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] != []:
                if graph[i][j][0] == 1:
                    shark1 += 1
                elif graph[i][j][0] > 1:
                    shark_other += 1
    if shark_other == 0:
        return False
    else:
        return True

N,M,K = map(int, input().split())
graph = [[list() for _ in range(N)] for _ in range(N)] # 그래프
shark_dir_dic = {} # 상어 좌표 담아둘 dict
for i in range(N):
    temp = list(map(int,input().split()))
    for j in range(N):
        if temp[j] != 0:
            graph[i][j].append(temp[j])
        if graph[i][j] != [] and graph[i][j][0] != 0:
            shark_dir_dic[graph[i][j][0]] = [i,j]

smell_graph = [[list() for _ in range(N)] for _ in range(N)] # 냄새 그래프
now_shark_dir = list(map(lambda x: int(x)-1, input().split())) # 현재 상어의 방향  
shark_dir = [[list() for _ in range(4)]  for _ in range(M)] # 상어 방향 우선순위 그래프

for i in range(M):
    for j in range(4):
        temp = list(map(lambda x: int(x)-1, input().split()))
        shark_dir[i][j].extend(temp)

time = 0
while time <= 1000:
    my_smell() # 냄새찍기
    move_shark() # 상어 이동시키기
    remove_shark() # 상어 중복 제거
    remove_smell() # 냄새 1 없애기
    if not check_shark1(): # 상어 1만 남아있는지 확인
        time += 1
        break
    time += 1

print(time if time <= 1000 else -1)