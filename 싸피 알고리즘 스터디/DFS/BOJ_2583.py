import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y):
    global cnt
    if x < 0 or x >= M or y < 0 or y >= N or graph[x][y] == 1:
        return
    graph[x][y] = 1
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)
    cnt += 1
    return cnt

M, N, K = map(int, input().split())
graph = [[0] * N for _ in range(M)]
ans = []

for _ in range(K):
    y1,x1,y2,x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1,y2):
            graph[i][j] = 1

for i in range(M):
    for j in range(N):
        if graph[i][j] == 0:
            cnt = 0
            ans.append(dfs(i,j))
print(len(ans))
print(*sorted(ans))
            