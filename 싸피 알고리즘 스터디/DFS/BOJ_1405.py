import sys
input = sys.stdin.readline

def dfs(x,y,cnt,percent):
    global res
    if not visited[x][y]:
        if cnt == N:
            res += percent
            return
        
        visited[x][y] = True
        for i in range(4):
            dfs(x+dir[i][0], y+dir[i][1], cnt+1, percent*percentages[i])
        visited[x][y] = False

N, East, West, South, North = map(int, input().split())
dir = [(0,1), (0,-1), (1,0), (-1,0)]
percentages = [East/100, West/100, South/100, North/100]
visited = [[False] * (100) for _ in range(100)]
total = 2**N
res = 0
num = 50

dfs(num,num,0,1)

print(res)