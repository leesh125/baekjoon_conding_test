import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0]
dy = [0,0,-1,1]
INF = int(1e9)

def findCustomer(startX,startY):
    if graph[startX][startY] >= 2:
        return startX,startY,graph[startX][startY],0

    q = deque()
    q.append((startX,startY,0))
    res = []
    visited = [[False] * N for _ in range(N)]
    visited[startX][startY] = True
    min_dist = INF

    while q:
        x,y,cnt = q.popleft()

        if cnt > min_dist: break
        
        if graph[x][y] >= 2:
            res.append([x,y,graph[x][y]])
            min_dist = cnt
            visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))
    if res:
        res.sort(key=lambda x:(x[0],x[1]))
        return res[0][0], res[0][1],res[0][2], min_dist
    return -1,-1,-1,-1

def findDestination(guestX,guestY,guestNum):
    q = deque()
    q.append((guestX,guestY,0))
    visited = [[False] * N for _ in range(N)]
    visited[guestX][guestY] = True

    while q:
        x,y,cnt = q.popleft()

        if guestNum in desti_graph[x][y]:
            desti_graph[x][y].remove(guestNum)
            return x,y,cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<N and not visited[nx][ny] and graph[nx][ny] != 1:
                visited[nx][ny] = True
                q.append((nx,ny,cnt+1))
    return -1,-1,-1


N,M,fuel = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
desti_graph = [[[] for _ in range(N)] for _ in range(N)]
taxiX,taxiY = map(int, input().split())
taxiX -= 1; taxiY -= 1
flag = False

for i in range(2,M+2):
    a,b,c,d = map(int, input().split())
    graph[a-1][b-1] = i # 손님 서 있는 위치
    desti_graph[c-1][d-1].append(i) # 목적지 위치

while M:
    guestX, guestY, guestNum, dist = findCustomer(taxiX,taxiY)
    graph[guestX][guestY] = 0
    if guestX == -1 or fuel < dist:
        fuel = -1
        break
    else:
        fuel -= dist
    
    destX,destY,dist2 = findDestination(guestX,guestY,guestNum)

    if dist2 == -1 or fuel < dist2:
        fuel = -1
        break
    else:
        fuel = fuel - dist2 + (dist2*2)
    M -= 1
    taxiX,taxiY = destX,destY
print(fuel)