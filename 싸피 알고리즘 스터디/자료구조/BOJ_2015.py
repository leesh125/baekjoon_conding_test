import sys
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0] * (N+1)
dp[0] = 0
ans = 0

for i in range(1,N+1):
    dp[i] = nums[i-1] + dp[i-1] # 누적합

dict = {}
for i in range(N,-1,-1): # 거꾸로
    ans += dict.get(dp[i] + K,0) # 현재 누적합 + K = 또다른 누적합 이 있으면 그 갯수만큼 +
    dict[dp[i]] = dict.get(dp[i],0) + 1 # 현재 누적합 추가해주기
print(ans)
# B - A = K
# B = A + K

# Good Explanation
import sys
case = sys.stdin.readline().strip().split()
N, K = int(case[0]), int(case[1])
A = list(map(int, sys.stdin.readline().strip().split()))
cnt, Sum, dic = 0, 0, {0: 1}
for i in range(N):
    Sum += A[i] # 누적합 (0~i번째 까지)
    if Sum - K in dic: # Sum을 만들 수 있는 누적합이 존재한다면
        cnt += dic[Sum - K] # 그 갯수만큼 cnt 더해줌
    if Sum in dic: # 누적합이 있으면 그만큼 +=1
        dic[Sum] += 1
    else: # 없으면 새로 1
        dic[Sum] = 1
print(cnt)