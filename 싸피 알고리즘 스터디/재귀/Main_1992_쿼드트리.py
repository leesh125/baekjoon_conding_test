import sys
input = sys.stdin.readline

def dfs(x,y,n):
    standard = graph[x][y]

    if n == 1:
        print(standard,end='')
        return

    for i in range(x, x+n):
        for j in range(y, y+n):
            if graph[i][j] != standard:
                print('(',end='')
                dfs(x,y,n//2)
                dfs(x,y+n//2,n//2)
                dfs(x+n//2,y,n//2)
                dfs(x+n//2,y+n//2,n//2)
                print(')',end='')
                return
    print(standard,end='')
    return
    
N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]

dfs(0,0,N)