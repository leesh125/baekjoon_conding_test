import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque()
    q.append([start,0])
    visited = [False] * 100001
    visited[start] = True

    while q:
        subin,cnt = q.popleft()

        if subin == K:
            return cnt

        for next_subin in [subin*2,subin-1, subin+1]:
            if 0 <= next_subin <= 100000 and not visited[next_subin]:
                visited[next_subin] = True
                if next_subin == subin*2:
                    q.append((next_subin, cnt))
                else:
                    q.append((next_subin, cnt+1))

N, K = map(int, input().split())
print(bfs(N))