import sys, heapq

input = sys.stdin.readline
INF = int(1e9)  # 무한대
T = int(input())  # 테케 수


def dijkstra(start):  # 다익스트라
    q = []
    heapq.heappush(q, (0, start))  # pq에 거리 0,시작점 추가
    distances = [INF] * (n + 1)  # 각 노드까지의 최단경로를 표시할 배열
    distances[start] = 0  # 시작점 ~ 시작점 거리 0

    while q:
        dist, now = heapq.heappop(q)  # 우선순위(최단 경로)가 높은 (거리, 현재노드)

        if dist > distances[now]:  # 현재 노드까지의 거리가 시작점부터 현재 노드까지의 최단 경로보다 크면
            continue  # 이미 방문한 곳임

        for g in graph[now]:  # 현재 노드에서 이어진 노드 그리고 그 거리
            cost = g[1] + dist  # 현재 노드까지의 거리 + 해당 노드까지의 거리

            if cost < distances[g[0]]:  # 위 비용이 해당 노드까지의 최단 경로보다 작으면
                distances[g[0]] = cost  # 갱신
                heapq.heappush(q, (cost, g[0]))  # 다음 방문할 곳 우선순위 q에 삽입
    return distances


for _ in range(T):
    n, m, t = map(int, input().split())  # 노드, 간선, 목적지 후보 갯수
    s, g, h = map(int, input().split())  # 시작점, 거쳐야할 두 점

    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))  # 양방향 간선

    shortest_start = dijkstra(s)  # 시작점부터 모든 점까지의 목적지
    shortest_g = dijkstra(g)  # 거치는 점1 부터 모든 점까지의 목적지
    shortest_h = dijkstra(h)  # 거치는 점2 부터 모든 점까지의 목적지

    ans = []

    for _ in range(t):
        des = int(input().rstrip())  # 목적지 후보
        # 시작점~거치는 점1 + 거쳐야할 간선 + 거치는 점2~목적지 or # 시작점~거치는 점2 + 거쳐야할 간선 + 거치는 점1~목적지
        if (
            shortest_start[des] == shortest_start[g] + shortest_g[h] + shortest_h[des]
            or shortest_start[des]
            == shortest_start[h] + shortest_h[g] + shortest_g[des]
        ):
            ans.append(des)  # 결과값에 목적지 추가
    print(*sorted(ans))  # 정렬 출력
