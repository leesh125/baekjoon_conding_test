import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline

def melting():
    global time
    melted = [0] * len(ice_list)
    for i in range(len(ice_list)):
        cnt = 0
        for dir in direction:
            if 0<=ice_list[i][0]+dir[0]<N and 0<=ice_list[i][1]+dir[1]<M and graph[ice_list[i][0]+dir[0]][ice_list[i][1]+dir[1]] == 0:
                cnt += 1
        melted[i] = cnt

    for i in range(len(ice_list)):
        if melted[i] >= graph[ice_list[i][0]][ice_list[i][1]]:
            graph[ice_list[i][0]][ice_list[i][1]] = 0
        else:
            graph[ice_list[i][0]][ice_list[i][1]] -= melted[i]

    time += 1
    visited = [[False] * M for _ in range(N)]
    for ice in ice_list:
        if graph[ice[0]][ice[1]] != 0:
            dfs(ice[0],ice[1],visited) # 임의의 빙산 탐색
            break

    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and not visited[i][j]:
                return 2 # 남은 빙산 있는데 분리되었다면

    temp_cnt = 0
    for ice in ice_list:
        if not visited[ice[0]][ice[1]]:
            temp_cnt += 1
    if temp_cnt==len(ice_list):
        return 3 # 남은 빙산 없을 때

    return 1 # 남은 빙산 있는데 분리 안되었다면(계속)


def dfs(x,y,visited):
    if 0>x or x>=N or 0>y or y>=M or graph[x][y] == 0 or visited[x][y]:
        return False

    visited[x][y] = True
    dfs(x+1,y,visited)
    dfs(x-1,y,visited)
    dfs(x,y+1,visited)
    dfs(x,y-1,visited)
    
    return True

direction = [(-1,0),(1,0),(0,-1),(0,1)]
N, M = map(int, input().split())
graph = []
ice_list = []
time = 0

for i in range(N):
    temp = list(map(int, input().split()))
    graph.append(temp)
    for j in range(M):
        if temp[j] != 0:
            ice_list.append([i,j])

flag = True
while flag:
    n = melting()
    if n == 1: # 남은 빙산 있는데 분리 안되었다면(계속)
        continue
    elif n == 2: # 남은 빙산 있는데 분리되었다면
        print(time)
        break
    elif n == 3: # 남은 빙산 없을 때(한번에 녹음)
        print(0)
        break
