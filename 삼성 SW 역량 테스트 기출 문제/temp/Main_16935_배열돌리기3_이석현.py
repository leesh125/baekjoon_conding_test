import sys
input = sys.stdin.readline

def one():
    for i in range(N//2):
        graph[i], graph[N-i-1] = graph[N-i-1], graph[i]

def two():
    for i in range(N):
        graph[i] = graph[i][::-1]

def three(graph):
    new_graph = [[0] * M for _ in range(N)]
    for j in range(N):
        for i in range(M-1,-1,-1):
            new_graph[j][M-1-i] = graph[i][j]
    return new_graph

def four(graph):
    new_graph = [[0] * M for _ in range(N)]
    for j in range(N-1,-1,-1):
        for i in range(M):
            new_graph[N-1-j][i] = graph[i][j]
    return new_graph

def five(graph):
    new_graph = [[0] * M for _ in range(N)]
    div_n = N//2; div_m = M//2
    
    for i in range(div_n+1):
        new_graph[i][div_m:] = graph[i][:div_m]
    for i in range(div_n):
        new_graph[i+div_n][div_m:] = graph[i][div_m:]
    for i in range(div_n,N):
        new_graph[i][:div_m] = graph[i][div_m:]
    for i in range(div_n):
        new_graph[i][:div_m] = graph[i+div_n][:div_m]

    return new_graph


def six(graph):
    new_graph = [[0] * M for _ in range(N)]
    div_n = N//2; div_m = M//2
    
    for i in range(div_n):
        new_graph[i+div_n][:div_m] = graph[i][:div_m]
    for i in range(div_n,N):
        new_graph[i][div_m:] = graph[i][:div_m]
    for i in range(div_n):
        new_graph[i][div_m:] = graph[i+div_n][div_m:]
    for i in range(div_n):
        new_graph[i][:div_m] = graph[i][div_m:]

    return new_graph

N, M, R = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
R_list = list(map(int, input().split()))

for r in R_list:
    if r == 1: one()
    elif r == 2: two()
    elif r == 3: N,M = M,N; graph = three(graph) 
    elif r == 4: N,M = M,N; graph = four(graph)
    elif r == 5: graph = five(graph)
    elif r == 6: graph = six(graph)

for g in graph:
    print(*g)

# Good Explanation
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
rs = list(map(int, input().split()))

for r in rs:
    if r == 1:
        arr = arr[::-1]
    elif r == 2:
        arr = [ar[::-1] for ar in arr]
    elif r == 3:
        arr = list(zip(*arr))
        arr = [ar[::-1] for ar in arr]
    elif r == 4:
        arr = list(zip(*arr))
        arr = arr[::-1]
    elif r == 5:
        n = len(arr)
        m = len(arr[0])
        temp = arr[n // 2:] + arr[:n // 2]
        for i in range(n // 2):
            arr[i] = temp[i][:m // 2] + arr[i][:m // 2]
        for i in range(n // 2, n):
            arr[i] = arr[i][m // 2:] + temp[i][m // 2:]
    elif r == 6:
        n = len(arr)
        m = len(arr[0])
        temp = arr[n // 2:] + arr[:n // 2]
        for i in range(n // 2):
            arr[i] = arr[i][m // 2:] + temp[i][m // 2:]
        for i in range(n // 2, n):
            arr[i] = temp[i][:m // 2] + arr[i][:m // 2]

for ar in arr:
    print(*ar)