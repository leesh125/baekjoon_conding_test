import sys
from collections import deque
input = sys.stdin.readline

def topology_sort():
    q = deque()
    res = []
    for i in range(1,N+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        res.append(now)

        for next in students[now]:
            indegree[next] -= 1
            if indegree[next] == 0:
                q.append(next)
    print(*res)

N,M = map(int, input().split())
students = [[] for _ in range(N+1)]
indegree = [0] * (N+1)
for _ in range(M):
    a,b = map(int, input().split())
    students[a].append(b)
    indegree[b] += 1

topology_sort()