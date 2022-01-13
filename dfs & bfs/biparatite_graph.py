import sys
sys.setrecursionlimit(10**6) # 재귀함수 깊이 제한 설정(Pypy 안먹힘)

# bfs 방법도 효율적일 수 있음(dfs는 메모리 초과일 수 있기에)
def dfs(now,color):
    global flag
    visited[now] = color
    for i in nodes[now]:
        if not visited[i]:
            dfs(i,color*-1)
        else:
            if visited[i] == visited[now]:
                flag = False

k = int(sys.stdin.readline())
ans = []
for _ in range(k):
    v, e = map(int, sys.stdin.readline().split())
    nodes = [[] for _ in range(v+1)]
    visited = [0] * (v+1) # 방문 처리(색깔을 저장할 곳)
    flag = True # 답을 가리는 flag
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        nodes[a].append(b) # 무방향 그래프라 둘 다 삽입
        nodes[b].append(a) # 무방향 그래프라 둘 다 삽입
    
    # 연결 그래프가 아닐 수 있기에 정점마다 방문을 한 적이 없으면 dfs 수행
    for i in range(1,v+1):
        if not visited[i]:  # 방문하지 않은 정점(노드)이라면
            visited[i] = 1 # 색깔(1)을 지정
            dfs(i,1) # dfs 수행 (dfs(i,visited[i])도 가능)

    ans.append("YES") if flag else ans.append("NO") # 이분 그래프 판별 플래그

for a in ans: # 답 출력
    print(a)

