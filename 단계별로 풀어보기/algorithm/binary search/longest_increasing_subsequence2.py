import sys


def upper_bound(ans, num):
    start = 0
    end = len(ans) - 1

    while start <= end:
        mid = (start + end) // 2

        if num > ans[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return start


N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
ans = []

for num in A:
    if len(ans) == 0:
        ans.append(num)
    else:
        if ans[-1] < num:
            ans.append(num)
        else:
            pos = upper_bound(ans, num)
            ans[pos] = num
print(len(ans))
