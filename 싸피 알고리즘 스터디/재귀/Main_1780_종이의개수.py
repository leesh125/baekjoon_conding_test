import sys
input = sys.stdin.readline

def check(x,y,n):
    if n == 1:
        ans[graph[x][y]] += 1
        return
    standard = graph[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if graph[i][j] != standard:
                for si in range(x, x+n, n//3):
                    for sj in range(y, y+n, n//3):
                        check(si,sj,n//3)
                return
    ans[graph[x][y]] += 1

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
ans = {-1:0,0:0,1:0}
check(0,0,N)
for value in ans.values():
    print(value)