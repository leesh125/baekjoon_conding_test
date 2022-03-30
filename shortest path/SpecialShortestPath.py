import sys, heapq

input = sys.stdin.readline
INF = int(1e9)  # 무한대

N, E = map(int, input().split())  # 노드, 간선 수
graph = [[] for _ in range(N + 1)]  # 간선의 비용을 담을 그래프

for i in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))  # 무(양)방향 그래프 (반대 방향도 꼭 추가하기!)

v1, v2 = map(int, input().split())  # 해당 두 정점을 무조건 지나야함

# 다익스트라 알고리즘
def dijkstra(start):
    distances = [INF] * (N + 1)  # 출발지 기점으로 타 노드 까지의 거리(초기: 무한대)
    q = []  # 최적의 해를 정렬할 그래프
    heapq.heappush(q, (0, start))  # 거리,출발지 = 0
    distances[start] = 0  # 출발지 ~ 출발지 거리 0

    while q:  # q에 계산할 해가 있는한
        dist, now = heapq.heappop(q)  # 계산된 현재 노드까지의 거리,현재 노드

        if dist > distances[now]:  # 계산된 현재 노드까지의 거리가 현재 노드의 최단경로보다 길면
            continue  # 비교 X

        for g in graph[now]:  # 현재 노드와 연결된 간선과 그 비용의 정보
            cost = dist + g[1]  # 계산된 현재 노드까지의 거리 + 연결된 해당 노드까지의 거리

            if cost < distances[g[0]]:  # 위 비용이 현재 노드의 최단 경로보다 작으면
                distances[g[0]] = cost  # 갱신
                heapq.heappush(q, (cost, g[0]))  # q에 추가(계속 연결된 지점을 찾을거기때문)

    return distances  # 거쳐가야하기에 출발지 기점 노드까지의 최단 경로를 담은 distances 반환


arr1, arr2, arr3 = dijkstra(1), dijkstra(v1), dijkstra(v2)  # 각 1, v1, v2 를 기점으로 최단경로 구함

res = []  # 결과를 담을 배열
res.append(arr1[v1] + arr2[v2] + arr3[N])  # 1 ~ v1 거치는 최단 + v1~v2  최단 + v2~목적지까지 최단
res.append(arr1[v2] + arr3[v1] + arr2[N])  # 1 ~ v2 거치는 최단 + v2~v1  최단 + v1~목적지까지 최단

if min(res) >= INF:  # 경로가 없으면 -1
    print(-1)
else:
    print(min(res))  # 둘 중 작은 값 반환
