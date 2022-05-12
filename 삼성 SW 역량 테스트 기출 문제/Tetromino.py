# My turn
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
max_num = 0 # 최댓값 담을 변수

def oneFour(): # 1 x 4 테트리스
    global max_num
    for i in range(N): # 1 X 4
        for j in range(M-3):
            max_num = max(max_num, sum(graph[i][j:j+4]))
    for i in range(N-3): # 4 X 1
        for j in range(M):
            max_num = max(max_num,graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+3][j])
            
def twoTwo(): # 2 X 2 테트리스 
    global max_num
    for i in range(N-1):
        for j in range(M-1):
            max_num = max(max_num, sum(graph[i][j:j+2]) + sum(graph[i+1][j:j+2]))
    

def threeTwo(): # ㄱ 자 테트리스
    global max_num
    for i in range(N-2): # 7 모양 테트리사
        for j in range(M-1):
            max_num = max(max_num, graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+2][j+1],
                                   graph[i][j+1]+graph[i+1][j+1]+graph[i+2][j]+graph[i+2][j+1],
                                   graph[i][j]+graph[i][j+1]+graph[i+1][j+1]+graph[i+2][j+1],
                                   graph[i][j]+graph[i][j+1]+graph[i+1][j]+graph[i+2][j])
    for i in range(N-1): # ㄱ 모양 테트리스
        for j in range(M-2): 
            max_num = max(max_num, graph[i][j]+graph[i+1][j]+graph[i+1][j+1]+graph[i+1][j+2],
                                   graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i+1][j],
                                   graph[i][j]+graph[i][j+1]+graph[i][j+2]+graph[i+1][j+2],
                                   graph[i+1][j]+graph[i+1][j+1]+graph[i+1][j+2]+graph[i][j+2])

def threeTwo2(): # 지그재그 테트리스
    global max_num
    for i in range(N-2): # 세로 지그재그 테트리스
        for j in range(M-1):
            max_num = max(max_num, graph[i][j]+graph[i+1][j]+graph[i+1][j+1]+graph[i+2][j+1],
                                   graph[i][j+1]+graph[i+1][j]+graph[i+1][j+1]+graph[i+2][j])
    for i in range(N-1): # 가로 지그재그 테트리스
        for j in range(M-2):
            max_num = max(max_num, graph[i][j]+graph[i][j+1]+graph[i+1][j+1]+graph[i+1][j+2],
                                   graph[i+1][j]+graph[i][j+1]+graph[i+1][j+1]+graph[i][j+2])
    
def twoThree(): # ㅗ 모양 테트리스
    global max_num
    for i in range(N-1): # ㅗ 모양 테트리스
        for j in range(M-2):
            max_num = max(max_num, sum(graph[i][j:j+3]) + graph[i+1][j+1])
            max_num = max(max_num, sum(graph[i+1][j:j+3]) + graph[i][j+1])
    for i in range(N-2): # ㅓ 모양 테트리스
        for j in range(M-1):
            max_num = max(max_num, graph[i][j]+graph[i+1][j]+graph[i+2][j]+graph[i+1][j+1],
                                   graph[i][j+1]+graph[i+1][j+1]+graph[i+2][j+1]+graph[i+1][j])
    
oneFour(),twoTwo(),threeTwo(),threeTwo2(),twoThree()
print(max_num) # 최댓값 구하기

# Good Explanation
import sys
input = lambda : sys.stdin.readline()

move = [(-1,0),(1,0),(0,-1),(0,1)] # 상,하,좌,우 이동

# dfs 탐색
def dfs(r, c, depth, s):
    global max_value

    # 현재 누적 값이 남은 탐색 숫자를 모두 그래프의 최댓값이라고 가정했을때 누적 최댓값 보다 작으면 비교 필요 x
    if s + maxv*(4-depth) <= max_value: 
        return        
    if depth >= 4: # 4번째 탐색이면
        if max_value < s:
            max_value = s # 비교후 최댓값 갱신
        return
    else: # 탐색 중이라면
        for dr, dc in move:
            nr, nc = r + dr, c + dc # 다음 이동할 좌표
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0: # 범위 내에 있고 방문 하지 않았다면
                if depth == 2: # 두번째 고른 사각형 일때는(보라색 ㅗ 모양 때문에)
                    visited[nr][nc] = 1 # 방문 처리
                    dfs(r, c, depth + 1, s + board[nr][nc]) # 현재값에서 dfs 수행
                    visited[nr][nc] = 0 # 재귀 끝나면 다시 돌리기

                visited[nr][nc] = 1
                dfs(nr, nc, depth + 1, s + board[nr][nc])
                visited[nr][nc] = 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

maxv = max(map(max, board)) # 그래프 중에서 가장 큰 값

max_value = 0 # 최댓값 저장할 변수
visited = [[0]*m for _ in range(n)] # 방문 표시

# 브루트 포수(완전 탐색)
for i in range(n):
    for j in range(m):
        visited[i][j] = 1 # 방문 처리
        dfs(i,j,1,board[i][j]) # 현재 행,열, 깊이, 현재 그래프 값 dfs 탐색
        visited[i][j] = 0 # 재귀 끝나면 다시 0으로

print(max_value)