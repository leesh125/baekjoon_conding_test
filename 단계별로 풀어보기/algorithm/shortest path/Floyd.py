import sys

input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for i in range(n + 1)]  # 인덱스를 기준으로 n~m까지의 거리를 표현할 그래프

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0  # 자기 자신 최단경로 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)  # a~b 까지의 비용 c

# 플로이드 워셜 알고리즘
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # i~j 최단 = i~k 최단 + k~j 최단
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):  # 출력
        print(graph[i][j], end=" ") if graph[i][j] != INF else print(0, end=" ")
    print()
