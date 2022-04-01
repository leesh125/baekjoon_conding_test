import sys

INF = int(1e9)
input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
distances = [INF] * (N + 1)  # 각 노드까지의 최소 거리 담을 배열

for _ in range(M):
    a, b, c = map(int, input().split())  # (현재 노드, 다음 노드, 까지 비용)
    graph.append((a, b, c))

# 벨만포드 알고리즘(최단 경로가 음수를 포함한 경우)
def bellman_ford(start):
    distances[start] = 0  # 시작점까지 최단경로 0

    # 반복을 정점 수 -1 만큼 하는 이유
    # : 1(현재)~최종 목적지 노드 까지의 최단경로의 길이는 전체 노드(N) -1(순환 포함 X)
    for i in range(N):
        for j in range(M):
            cur_node = graph[j][0]  # 현재 노드
            next_node = graph[j][1]  # 다음 노드
            cost = graph[j][2]  # 그 비용

            if (  # 도달할 수 없는 곳이 아니고 다음 노드 최단 경로가 현재 노드 최단 경로 + 다음노드까지의 비용보다 크면
                distances[cur_node] != INF
                and distances[next_node] > distances[cur_node] + cost
            ):
                distances[next_node] = distances[cur_node] + cost  # 값 갱신
                if i == N - 1:  # 마지막 까지 갱신이 되었다면 순회(무한 루프)이기에
                    return True  # flag 설정

    return False


negative_cycle = bellman_ford(1)

if negative_cycle:  # 무한 순회면
    print(-1)  # -1
else:
    for i in range(2, N + 1):  # 1번을 제외한 노드
        if distances[i] == INF:  # 해당 노드에 도달할 수 없으면 -1 출력
            print(-1)
        else:
            print(distances[i])  # 해당 노드까지의 거리 출력
