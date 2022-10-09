import sys
input = sys.stdin.readline
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
divide_candidate = set()

def move_fireballs():    
    global graph
    
    new_graph = [[[] for _ in range(n+1)] for _ in range(n+1)]
    for x in range(n):
        for y in range(n):
            if not graph[x][y]:
                continue
            while graph[x][y]:
                m,s,d = graph[x][y].pop()
                nx = (x + (dx[d] * s)) % n
                ny = (y + (dy[d] * s)) % n
                
                new_graph[nx][ny].append([m,s,d])
                if len(new_graph[nx][ny]) >= 2:
                    divide_candidate.add((nx,ny))
            graph[x][y] = []
    graph = new_graph
    return divide_candidate

def make_fireballs():
    global divide_candidate
    dir1 = [0,2,4,6]
    dir2 = [1,3,5,7]

    for x,y in divide_candidate:
        total_m, total_s = 0,0
        odd_cnt = 0; even_cnt = 0
        len_fireballs = len(graph[x][y])
        for i in range(len(graph[x][y])):
            m,s,d = graph[x][y][i]
            total_m += m; total_s += s
            if d % 2 == 1: odd_cnt += 1
            else: even_cnt += 1
        m = total_m // 5
        if m == 0:
            graph[x][y] = []
            continue
        graph[x][y] = []
        s = total_s // len_fireballs

        dir = dir1 if odd_cnt == 0 or even_cnt == 0 else dir2
        for d in dir:
            graph[x][y].append([m,s,d])
    divide_candidate = set()
    

n,m,k = map(int, input().split())
graph = [[[] for _ in range(n)] for _ in range(n)]

for i in range(m):
    r,c,m,s,d = map(int, input().split())
    graph[r-1][c-1].append([m,s,d])

while k > 0:
    move_fireballs()
    make_fireballs()
    k -= 1

ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]:
            for g in graph[i][j]:
                ans += g[0]
print(ans)