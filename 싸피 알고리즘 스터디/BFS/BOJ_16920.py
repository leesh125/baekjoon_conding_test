import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    flag = True 
    while flag: # 더 이상 이동이 없을때까지
        flag = False
        for i in range(1, players+1): # 1번부터 순차적으로 큐
            if not q_list[i]: 
                continue
            q = q_list[i]
            for _ in range(S[i-1]): # 플레이어가 이동할 수 있을만큼 반복(큐 삭제 추가되면서 자동으로 추가 좌표만 큐에 남기에 ㄱㅊ)
                for _ in range(len(q)): # 큐 길이(한 라운드)만큼만 성 짓기
                    
                    x, y = q.popleft() # 좌표

                    for dir in range(4):
                        nx = x + dx[dir]
                        ny = y + dy[dir]
                        # 다음 좌표가 땅이라면
                        if 0<=nx<N and 0<=ny<M and not visited[nx][ny]:
                            q.append((nx,ny)) # 큐에 다음좌표 추가(다음 라운드때 실행됨)
                            visited[nx][ny] = True # 성 짓기
                            ans[i] += 1  # 성 갯수 +1
                            flag = True # 이동했으니 True
                if not q: # 여기에 놓아야 S만큼 안돔
                    break # 큐 없으면 빠지기

N, M, players = map(int, input().split())
S = list(map(int, input().split()))
graph = []
visited = [[False] * M for _ in range(N)]
ans = [0] * (players+1)
dx = [-1,1,0,0]
dy = [0,0,-1,1]
q_list = [deque() for _ in range(players+1)] # 각 플레이어마다의 자리 큐

for i in range(N):
    temp = list(input().rstrip())
    graph.append(temp)
    for j in range(M):
        now = temp[j]
        if now == '#':
            visited[i][j] = True
        elif now != '.': # 플레이어의 성이면
            p = int(now)
            visited[i][j] = True
            q_list[p].append((i,j)) # 지금 좌표 플레이어큐에 삽입
            ans[p] += 1 # 플레이어 성 갯수 +1
bfs() # bfs
print(*ans[1:])