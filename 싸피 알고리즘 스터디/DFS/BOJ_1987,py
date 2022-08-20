import sys
input = sys.stdin.readline

def dfs(x,y,cnt,arr):
    global ans

    ans = max(ans,cnt)

    for d in dir:
        nx = x + d[0]
        ny = y + d[1]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        alpha = ord(graph[nx][ny])-65
        if arr[alpha] == 0:
            arr[alpha] += 1
            dfs(nx,ny,cnt+1,arr)
            arr[alpha] -= 1

dir = [(-1,0),(1,0),(0,-1),(0,1)]
N, M = map(int, input().split())
graph = [list(input().rstrip()) * M for _ in range(N)]
ans = 0

arr = [0] * (90-65+1)
arr[ord(graph[0][0])-65] += 1
dfs(0,0,1,arr)
print(ans)