# My turn
import sys
input = sys.stdin.readline

N,L = map(int,input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cnt = 0 # 지나갈 수 있는 길의 갯수 cnt

def all_same(line): # 현재 길의 높이가 모두 같은지 체크
    for i in range(len(line)-1): # 줄 길이 순회
        if line[i] != line[i+1]: # 다른게 있으면
            return False # false
    return True # 다 같으면 true

def check(line): # 경사로를 놓을 수 있는지 체크하는 함수
    len_line = len(line) # 줄 길이
    visited = [0] * len_line # 방문 처리
    for i in range(len_line-1): # 줄 길이 -1 만큼 순회
        if line[i] != line[i+1]: # 다른 값일 때
            if abs(line[i] - line[i+1]) > 1: # 차이가 1보다 크면
                return False # 안됨
            else: # 둘의 차이가 1보다 작을 때
                if line[i] < line[i+1]: # 다음것이 더 큰거면(오르막 경사)
                    if i+1 < L: # 높이가 다른데 경사로를 앞에 놓을 수 없을때
                        return False # false
                    # 경사로를 놓는곳이 같은 높이가 아니거나 이미 경사가 세워진 곳이면
                    if not all_same(line[i+1-L:i+1]) or sum(visited[i+1-L:i+1]) != 0:
                        return False # false
                    else:
                        for j in range(i+1-L,i+1): 
                            visited[j] = 1 # 방문처리(오르막 경사로 세움)
                elif line[i] > line[i+1]: # 다음것이 더 큰거면(내리막 경사)
                    if i + L >= N: # 높이가 다른데 경사로를 더이상 뒤로 놓을 수 없을때
                        return False # false
                    # 경사로를 놓는곳이 같은 높이가 아니거나 이미 경사가 세워진 곳이면
                    if not all_same(line[i+1:i+1+L]) or visited[i+1]: 
                        return False # false
                    else:
                        for j in range(i+1,i+1+L):
                            visited[j] = 1 # 방문처리(내리막 경사로 세움)
    return True  # 조건이 모두 충족하면 True
for g in graph: # 행 비교 그래프
    if all_same(g): # 모두 같거나
        cnt += 1
    elif check(g): # 조건에 부합되면
        cnt += 1

for r_g in zip(*graph): # 열 그래프
    if all_same(r_g):
        cnt += 1
    elif check(r_g):
        cnt += 1
print(cnt)

# Good Explanation
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def check():
  global res
  for i in range(n):
    h = board[i][0] # 각 행의 처음 값 대입
    cnt = 1 # stack = 1(처음 값)
    for j in range(1, n): # 1~끝까지
      if board[i][j] == h: # 다음 것과 같다면 통과
        cnt += 1 # 스택길이 += 1
      elif board[i][j] == h+1 and cnt >= 0: # 오르막 경사일 때
        if cnt >= l: # 여태 건넌 칸이 똑같은 크기였다면
          h = board[i][j] # 높이를 h로
          cnt = 1 # cnt 1로 초기화
        else: # 여태 건넌 칸이 똑같은 크기가 아니라면 
          break # 빠져나오기
      elif board[i][j] == h-1 and cnt >= 0: # 내리막 경사일떼
        h = board[i][j] # 높이를 h로
        cnt = -l + 1 # cnt를 -경사로 길이 + 1 로 변환(추후에 해당 높이와 같은 것이 경사로 길이만큼 있어야함 그래야 양수됨)
      else: # 그 외에는 빠져나오기
        break
    else: # 안빠져나오고 수행이 잘 되었을떄
      if cnt >= 0: # 스택 길이가 0보다 크거나 같으면 
        res += 1 # 결과 += 1

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0

check() # check 함수 실행
board = list(zip(*board)) # 열,행 변경
check() # check 함수 실행
print(res)