import sys, heapq

INF = int(1e9)  # 무한대
input = sys.stdin.readline


def dijkstra(start, graph, N, M):  # 다익스트라
    q = []
    heapq.heappush(q, (0, 0, start))  # 거리, 비용, 현재 노드
    # 각 도시(행)에서 해당 비용(열)으로 목적지까지 갈 수 있는 최소 비용
    distances = [[INF] * (M + 1) for _ in range(N + 1)]

    while q:
        # 현재 까지 거리, 현재까지 비용, 현재 도시
        cur_dist, cur_cost, now = heapq.heappop(q)

        # 현재까지 거리가 현재 도시에서 현재 비용으로 갈 수 있는 최단 경로보다 크면
        if cur_dist > distances[now][cur_cost]:
            continue  # 갱신할 필요 없음

        # 다음 도시, 다음 도시까지 비용, 다음 도시까지 거리(현재 도시에서부터)
        for next_node, next_cost, next_dist in graph[now]:
            total_dist = cur_dist + next_dist  # 현재 까지 거리 + 다음 도시로 갈 거리
            total_cost = cur_cost + next_cost  # 현재 까지 비용 + 다음 도시로 갈 비용

            # 현재 도시까지의 누적 비용이 주어진 비용보다 적거나,
            # 현재 까지 거리 + 다음 도시로 갈 거리가 다음 도시의 현재 비용으로 갈 수 있는 거리보다 작으면 (갱신)
            if total_cost <= M and total_dist < distances[next_node][total_cost]:
                for i in range(total_cost, M + 1):  # 현재 까지 비용 + 다음 도시로 갈 비용 부터 최종 가격까지
                    # distances[next_node][i] = min(distances[next_node][i], total_dist)

                    # 현재 까지 거리 + 다음 도시로 갈 거리가 기존에 있는 비용으로 갈 수 있는 거리보다 작으면 갱신
                    if total_dist >= distances[next_node][i]:
                        break
                    distances[next_node][i] = total_dist
            else:
                continue
            heapq.heappush(q, (total_dist, total_cost, next_node))
    return min(distances[N])  # 마지막 도시까지 해당 비용으로 갈 수 있는 최단경로의 집합


for _ in range(int(input())):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))

    ans = dijkstra(1, graph, N, M)
    if ans != INF:  # 최단경로가 있으면
        print(ans)  # 출력
    else:
        print("Poor KCM")  # 없으면 이거 출력
