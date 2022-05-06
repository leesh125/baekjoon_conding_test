from sys import stdin

# 가장 긴 증가하는 부분 수열 
def up(seq, n):

    for i in range(1, n):
        for j in range(i):
            if seq[j] < seq[i]:
                d_up[i] = max(d_up[j] + 1, d_up[i])

    return d_up

# 가장 긴 감소하는 부분 수열
def down(seq, n):

    seq.reverse()
    for i in range(1, n):
        for j in range(i):
            if seq[i] > seq[j]:
                d_down[i] = max(d_down[j] + 1, d_down[i])

    return d_down


n = int(stdin.readline())
seq = list(map(int, stdin.readline().split()))
d_up = [1] * n # 가장 긴 증가하는 부분 수열의 길이를 담음
d_down = [1] * n # 가장 긴 감소하는 부분 수열의 길이를 담음

# 가장 긴 증가 or 감소 부분수열 길이 값 얻기
d_up, d_down = up(seq, n), down(seq, n) 

# 오르내리는 부분 수열 길이의 기준 0번째
ans = d_up[0] + d_down[-1] - 1

for i in range(1, n):
    if ans < d_up[i] + d_down[(n - i - 1)] - 1: # 둘의 합 최댓값 갱신
        ans = d_up[i] + d_down[(n - i - 1)] - 1
print(ans)
