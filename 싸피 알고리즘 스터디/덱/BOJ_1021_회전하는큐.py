import sys
from collections import deque
input = sys.stdin.readline

N,M = map(int,input().split())
nums = list(map(int,input().split()))
lenq = N
cnt = 0

q = deque(list(range(1,N+1)))

for n in nums:
    if q[0] == n:
        q.popleft()
        lenq -= 1
    else:
        idx = q.index(n)
        if idx+1 <= lenq // 2 + 1:
            for _ in range(idx):
                q.rotate(-1) # 2번 연산(왼쪽으로 한 칸)
            cnt += idx
        else:
            for _ in range(lenq-idx):
                q.rotate() # 3번 연산(오른쪽으로 한 칸)
            cnt += lenq-idx
        lenq -= 1
        q.popleft()
print(cnt)