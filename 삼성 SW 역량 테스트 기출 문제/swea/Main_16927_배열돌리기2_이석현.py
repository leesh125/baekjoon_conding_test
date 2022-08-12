import sys
input = sys.stdin.readline

def getCircle(N,M,start):
    circle = []
    for i in range(start, N-start-1):
        circle.append(graph[i][start])
    for j in range(start, M-start-1):
        circle.append(graph[N-start-1][j])
    for i in range(N-start-1,start,-1):
        circle.append(graph[i][M-start-1])
    for j in range(M-start-1,start,-1):
        circle.append(graph[start][j])
    
    return circle
    
def match(circle):
    idx = 0
    for i in range(start, N-start-1):
        graph[i][start] = circle[idx]
        idx += 1
    for j in range(start, M-start-1):
        graph[N-start-1][j] = circle[idx]
        idx += 1
    for i in range(N-start-1,start,-1):
        graph[i][M-start-1] = circle[idx]
        idx += 1
    for j in range(M-start-1,start,-1):
        graph[start][j] = circle[idx]
        idx += 1

def rotate(N,M,cnt,start):
    circle = getCircle(N,M,start)
    idx = cnt % len(circle)
    circle = circle[-idx:] + circle[:-idx]
    match(circle)

N, M, cnt = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]

for start in range(min(N,M)//2):
    rotate(N,M,cnt,start)

for g in graph:
    print(*g)