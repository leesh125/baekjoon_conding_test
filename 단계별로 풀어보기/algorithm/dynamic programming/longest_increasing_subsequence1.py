from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
d = [1] * n

for i in range(1, n):  # 두번째 항목부터
    for j in range(i):  # 수열 길이 합 누적
        if nums[j] < nums[i]:  # 현재 숫자가 이전 것보다 크면
            d[i] = max(d[j] + 1, d[i])  # 누적 합 비교 후 갱신
print(max(d))
