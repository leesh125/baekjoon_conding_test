n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
cnt = 0

for i in reversed(range(len(arr))):
    if k // arr[i] != 0:
        cnt += k // arr[i]
        k %= arr[i]
    else:
        continue

print(cnt)