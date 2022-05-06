import sys
# 재귀를 사용하기 위해선 필수로 입력해야 할 코드
# 파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다. 
# 따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 되는데, 
# 문제는 코딩테스트 환경에서는 에러 메시지를 볼 수 없다는 것이다.
sys.setrecursionlimit(10 ** 6)

# from collections import deque

# bfs 방법 - stack을 사용해야함
# def bfs(x, y):
#     stack = [(x, y)]
#     graph[x][y] = 2
#     while stack:
#         x, y = stack.pop()
#         for i, j in (0, 1), (0, -1), (1, 0), (-1, 0):
#             x2, y2 = x + i, y + j
#             if x2 > N-1 or y2 > M-1 or x2 < 0 or y2 < 0:
#                 continue
#             if graph[x2][y2] == 1:
#                 stack.append((x2, y2))
#                 graph[x2][y2] = 2

# dfs 함수
def dfs(x,y):
    if x <= -1 or x >= n or y <= -1 or y >= m: # 범위를 벗어날 경우
        return False
    
    if graph[x][y] == 1: # 배추가 있는 곳이면
        graph[x][y] = 0 # 0으로 방문 표시를

        # 재귀 수행
        dfs(x-1,y) 
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x, y+1)
        return True
    return False

        

test = int(sys.stdin.readline())



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
ans = []

# test 만큼 반복
for _ in range(test):
    res = 0

    m, n, cnt = list(map(int,sys.stdin.readline().split()))
    graph = [[0] * m for _ in range(n)]

    for _ in range(cnt):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1 # y, x 바꿔서 리스트에 순차적으로 저장

    for i in range(n):
        for j in range(m):
            if dfs(i,j) == True: # true일 때 재귀가 다 끝나면
                res += 1  # res + 1
    
    ans.append(res)

for i in ans:
    print(i)
