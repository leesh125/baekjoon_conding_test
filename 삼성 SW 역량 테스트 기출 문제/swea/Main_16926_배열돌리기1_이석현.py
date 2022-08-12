import sys
input = sys.stdin.readline

N, M, cnt = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
small = M if N > M else N
tmpN, tmpM = N, M

for _ in range(cnt):
    for i in range(small//2):
        x,y = i,i
        temp = graph[x][y]

        for j in range(i+1, N-i): # 밑으로
            x = j
            next = graph[x][y]
            graph[x][y] = temp
            temp = next

        for j in range(i+1, M-i): # 오른쪽으로
            y = j
            next = graph[x][y]
            graph[x][y] = temp
            temp = next
        
        for j in range(N-i-2, i-1,-1): # 위로
            x = j
            next = graph[x][y]
            graph[x][y] = temp
            temp = next

        for j in range(M-i-2,i-1,-1): # 왼쪽으로
            y = j
            next = graph[x][y]
            graph[x][y] = temp
            temp = next

for g in graph:
    for n in g:
        print(n, end=' ')
    print()
