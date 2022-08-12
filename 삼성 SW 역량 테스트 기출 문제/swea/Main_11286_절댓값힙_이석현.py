import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, (abs(num),num))
    else:
        print(heapq.heappop(heap)[1] if heap else 0)
