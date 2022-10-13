import sys
input = sys.stdin.readline

def check(graph):
    for j in range(1,N+1):
        col = j
        for i in range(1,H+1):
            if graph[i][col]:
                col += 1
            elif 1 < col and graph[i][col-1]:
                col -= 1
        if col != j:
            return False
    return True

def dfs(i,j,ladder_cnt,ladder_max_cnt, graph):
    global ans
    if ladder_cnt == ladder_max_cnt:
        if check(graph):
            ans = ladder_max_cnt
        return
    for x in range(i,H+1):
        for y in range(j,N):
            if graph[x][y] != 1:
                if 1 < y and graph[x][y-1] == 1:
                    continue
                if y < N and graph[x][y+1] == 1:
                    continue

                graph[x][y] = 1
                dfs(x,y,ladder_cnt+1,ladder_max_cnt,graph)
                graph[x][y] = 0

N,M,H = map(int,input().split())
graph = [[0] * (N+1) for _ in range(H+1)]
copy_graph = [list() for _ in range(H+1)]
ans = -1
for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1

for h in range(4):
    for i in range(H+1):
        copy_graph[i] = graph[i][:]
    dfs(1,1,0,h,copy_graph)
    if ans != -1: break

print(ans)


# Good Explanation
from sys import stdin as f

from itertools import combinations

def simulate(i):
    row = 0
    result = i
    while row < H:
        if board[row][result] == 1:
            result += 1
        elif board[row][result] == 2:
            result -= 1
        row += 1
    return result

def check():
    diff = 0
    for i in range(N):
        if simulate(i) != i:
            diff += 1
    return diff

def combination(arr,N):
    result = []

    if N == 0:
        return [[]]

    for i in range(len(arr)):
        elem = arr[i]
        for rest in combination(arr[i+1:],N-1):
            result.append([elem] + rest)
    return result

N,M,H = map(int,f.readline().split())
board = [[0 for i in range(N)] for _ in range(H)]
answer = float('inf')
for _ in range(M):
    a,b = map(int,f.readline().split())
    a,b = a-1,b-1
    board[a][b] = 1
    board[a][b+1] = 2
candidate = []

for i in range(H):
    for j in range(N-1):
        if board[i][j] == 0 and board[i][j+1] == 0:
            candidate.append((i,j))
if check() > 6:
    print(-1)
    exit()
ck = 0
for i in range(4):
    for seq in combination(candidate,i):
        for x,y in seq:
            if board[x][y] != 0:
                break
            board[x][y] = 1
            board[x][y+1] = 2
        else:
            if check() == 0:
                answer = i
                ck = 1
                break
        for x,y in seq:
            board[x][y] = 0
            board[x][y+1] = 0
    if ck == 1:
        break
print(answer if answer != float('inf') else -1)