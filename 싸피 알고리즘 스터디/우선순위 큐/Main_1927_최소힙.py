import sys,heapq
input = sys.stdin.readline
hq = []
for _ in range(int(input())):
    cmd = int(input())
    if cmd == 0:
        if len(hq) == 0: print(0)
        else:
            print(heapq.heappop(hq))
    else:
        heapq.heappush(hq, cmd)