import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
nums = [(i+1) for i in range(N)]
cnt = 0

q = deque()
for i in range(N):
    q.append(i+1)

print('<',end='')
while q:
    for i in range(K-1):
        n = q.popleft()
        q.append(n)
    cnt += 1
    if cnt != N:
        print(q.popleft(),end=', ')
    else:
        print(q.popleft(),end='')
print('>',end='')