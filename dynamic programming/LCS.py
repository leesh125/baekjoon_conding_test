# My turn
from sys import stdin

arr1 = stdin.readline().rstrip()
arr2 = stdin.readline().rstrip()
l1 = len(arr1)
l2 = len(arr2)
d = [[0] * (l2 + 1) for _ in range(l1 + 1)]  # 두 문자열을 각각 비교하기 위한 배열

for i in range(1, l1 + 1):
    for j in range(1, l2 + 1):
        if arr1[i - 1] == arr2[j - 1]:  # 만약 문자가 같다면 각 문자를 추가하기전 lcs+1
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])  # 각 문자열의 한 문자씩의 최댓값비교

print(d[-1][-1])

# Good Explanation
s1 = input()
s2 = input()

len_s1, len_s2 = len(s1), len(s2)
dp = [0] * (len_s1)

for i in range(len_s2):
    cnt = 0
    for j in range(len_s1):
        if cnt < dp[j]:  # 해당 자리 누적값이 현재 누적값보다 크면
            cnt = dp[j]  # 현재 누적값 갱신
        elif s2[i] == s1[j]:  # 만약 같다면
            dp[j] = cnt + 1  # 해당 자리 누적값 +1
print(max(dp))
