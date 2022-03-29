import sys, heapq

input = sys.stdin.readline
INF = int(1e9)  # 무한대

V, E = map(int, input().split())  # 노드, 간선
start = int(input())  # 시작점
graph = [[] for _ in range(V + 1)]  # 간선과 비용을 담은 그래프
distance = [INF] * (V + 1)  # 각 노드당 최단거리를 담는 그래프

for _ in range(E):
    a, b, c = map(int, input().split())  # a노드에서 b노드로 가는 비용 c
    graph[a].append((b, c))

# pq 다익스트라 알고리즘
def dijkstra(start):
    q = []  # 우선순위 큐
    heapq.heappush(q, (0, start))  # 우선순위 큐 삽입(거리오름차순 으로)
    distance[start] = 0  # 시작점의 최소비용은 0

    while q:
        dist, now = heapq.heappop(q)  # 우선순위 큐에서 pop(현재 노드의 최단비용,현재 노드)

        if distance[now] < dist:  # 현재 노드에 최단 거리가 큐에 있는 현재 노드 최단거리 작으면
            continue  # 갱신 안함(이미 방문한 노드임)

        for g in graph[now]:  # 현재 노드와 이어진 노드, 그 비용
            cost = dist + g[1]  # 현재 노드 최단거리 + 이어진 다른 노드까지의 거리

            if cost < distance[g[0]]:  # 그 비용이 현재 노드에 최단 거리보다 작으면
                distance[g[0]] = cost  # 갱신
                heapq.heappush(q, (cost, g[0]))  # 큐에 삽입


dijkstra(start)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
