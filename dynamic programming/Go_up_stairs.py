import sys

def step(n):
    dp[0] = stairs[0] # dp 테이블에 대응
    dp[1] = max(stairs[1], stairs[1] + dp[0])
    dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, n): # 점화식 구현(두칸 전의 비용 + 현재 비용 : 세칸전의 비용 + 한칸 전의 비용 + 현재비용)
        dp[i] = max(dp[i - 2] + stairs[i], dp[i - 3] + stairs[i - 1] + stairs[i])
    return dp[-1]

n = int(sys.stdin.readline())
stairs = [0] * n
dp = [0] * n
for i in range(n):
    stairs[i] = int(sys.stdin.readline())

if n == 1: # 계단이 한칸일 경우 
    print(stairs[0]) # 그대로 비용 출력
elif n == 2: # 계단이 두칸일 경우
    print(sum(stairs)) # 더한 비용을 출력(최대값)
else:
    print(step(n))
