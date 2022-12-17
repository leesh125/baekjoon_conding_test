import sys
input = sys.stdin.readline
arr = list(range(1,21))
for _ in range(10):
    start,end = map(int,input().split())
    if start-2 == -1:
        arr[start-1:end] = arr[end-1::-1]
    else:
        arr[start-1:end] = arr[end-1:start-2:-1]
print(*arr)