import sys
from collections import deque

def bfs(n,x,y):
    queue = deque()
    queue.append((x,y)) # 현재 위치 큐에 추가
    visited = [[0] * chess_size[n] for _ in range(chess_size[n])] # 재방문을 방지하기 위한 visited 배열

    while queue:
        a,b = queue.popleft()

        if a == pos[n][1][0] and b == pos[n][1][1]: # 목표위치에 도착했다면
            print(visited[a][b]) # 출력
            return 0

        for i in range(8): # 나이트의 이동할 수 있는 횟수 만큼
            na = a + dx[i]
            nb = b + dy[i]

            # 범위를 초과하지 않고 방문한 좌표가 아니라면 이동
            if 0<=na<chess_size[n] and 0<=nb<chess_size[n] and visited[na][nb] == 0:
                visited[na][nb] = visited[a][b] + 1
                queue.append((na,nb))

n = int(sys.stdin.readline().rstrip())
chess_size = []
pos = []
for i in range(n):
    temp = []
    chess_size.append(int(sys.stdin.readline().rstrip())) # n번 입력 받은 만큼의 체스 크기 배열 저장
    for _ in range(2):
        temp.append(list(map(int, sys.stdin.readline().split())))  # n번 입력 받은 만큼의 현재 위치와 목표 위치 배열에 저장
    pos.append(temp)
dx = [1,2,2,1,-1,-2,-2,-1] # 나이트의 x 이동
dy = [2,1,-1,-2,-2,-1,1,2] # 나이트의 y 이동

for i in range(n):
    bfs(i,pos[i][0][0],pos[i][0][1]) # 입력받은 케이스 수 만큼 현재 위치와 목표위치 n번만큼 bfs 수행
