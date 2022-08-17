import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    global cnt
    if x < 0 or y < 0 or x >= N or y >= M:
        return False
    if graph[x][y] == 1:
        cnt += 1
        graph[x][y] = 0
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
ans = [0]

for i in range(N):
    for j in range(M):
        if dfs(i,j):
            ans.append(cnt)
            cnt = 0
print(len(ans)-1)
print(max(ans))