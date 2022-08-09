from collections import deque
import sys
input = sys.stdin.readline

def bfs(i,j,cnt): # bfs
    q.append((i,j,cnt)) # x,y좌표와 걸린시간 cnt
    visited[i][j] = True # 현재 좌표 방문처리
    min_cnt = 100000 # 최솟값 비교하기 위한 max 걸린시간
    while q: # 큐에 값이 있을동안
        x,y,now_cnt = q.popleft() # x,y좌표와 걸린시간 cnt
        
        if x == N-1 and y == M-1: # 끝가지오면
            min_cnt = min(min_cnt, now_cnt) # cnt 값 최솟값 비교후 저장

        for i in range(4): # 상,하,좌,우
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny]: # 방문 X & 범위 내
                if graph[nx][ny] == 2: # 검이라면
                    visited[nx][ny] = True # 방문하고
                    q.append((nx,ny,now_cnt+1)) # 큐에 추가
                    min_cnt = min(min_cnt,bfs2(nx,ny,now_cnt+1)) # bfs2 돌리기
                    graph[nx][ny] == 0 # 검 줍기
                elif graph[nx][ny] != 1: # 검이 아니라 0이라면
                    visited[nx][ny] = True # 방문처리
                    q.append((nx,ny,now_cnt+1)) # 큐에 추가
    return min_cnt # 최솟값 반환

def bfs2(i,j,cnt): # 검을 집은 후 bfs
    q2 = deque()
    q2.append((i,j,cnt))
    min_cnt2 = 100000
    new_visited[i][j] = True
    while q2:
        x,y,now_cnt = q2.popleft()
        
        if x == N-1 and y == M-1:
            min_cnt2 = min(min_cnt2, now_cnt)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0<=nx<N and 0<=ny<M and not new_visited[nx][ny]:
                new_visited[nx][ny] = True
                q2.append((nx,ny,now_cnt+1))
    return min_cnt2   

dx = [-1,1,0,0]
dy = [0,0,-1,1]
N, M, T = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)] # 방문처리
new_visited = [[False] * M for _ in range(N)] # 검을 잡은 뒤에 방문처리
q = deque()
ans = bfs(0,0,0) # bfs 시작
print(ans if ans <= T else 'Fail') # 제한 시간내에 구하면 그 값 출력

# Good Explanation
import sys


def sol():
    input = sys.stdin.readline
    N, M, T = map(int, input().split(" "))
    castle = []
    for i in range(N):
        castle.append(list(map(int, input().split(" "))))
    visited = [[False for j in range(M)] for i in range(N)]
    print(bfs(N, M, T, castle, visited))


def bfs(N, M, T, castle, visited):#bfs
    gram = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    q = []
    visited[0][0] = True
    q.append((0, 0, 0))
    while len(q) > 0: # 큐에 값이 있을동안
        x, y, count = q.pop(0)
        if castle[x][y] == 2: # 현재 도달한 곳이 검이라면
            gram = count + ((N - 1) - x) + ((M - 1) - y) # 지금까지 걸린시간 + 끝까지 직진 ㄱ밧
        if x == N - 1 and y == M - 1: # 끝이라면
            time = count
            if gram != 0:
                time = min(count, gram) # 검 집은 후 걸린시간 vs 걸린 시간
            if time <= T: # 시간 안에 구했다면
                return time # 그 값 출력
            return "Fail"
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visited[nx][ny] and castle[nx][ny] != 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, count + 1))
    if gram != 0 and gram <= T:
        return gram
    return "Fail"


if __name__ == "__main__":
    sol()