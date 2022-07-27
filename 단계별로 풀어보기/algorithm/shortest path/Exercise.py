import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한대(도달할 수 없는 지점)

V, E = map(int, input().split())
graph = [[INF] * (V + 1) for _ in range(V + 1)]  # i~j 까지 최단 경로

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c  # 그래프에 최단경로 추가

for k in range(1, V + 1):  # 매개체
    for i in range(1, V + 1):  # 행
        for j in range(1, V + 1):  # 열
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])  # 최솟값 갱신

ans = INF  # 정답을 나타낼 변수
for diagonal in range(1, V):  # 대각선
    for i in range(1, V - diagonal + 1):  # 행
        j = i + diagonal  # 열

        # ex) 1을 시작/목적으로 하는 사이클의 최단 경로는
        # 1~2 최단경로 + 2~1 최단경로 , 1~3 최단경로 + 3~1 최단경로...
        ans = min(ans, graph[i][j] + graph[j][i])  # 최솟값 갱신
print(ans) if ans != INF else print(-1)  # 도달할 수 없으면 -1 아니면 값 출력
