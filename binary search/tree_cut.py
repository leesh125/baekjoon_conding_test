# My turn
import sys
n, m = map(int,sys.stdin.readline().split())
tree = list(map(int,sys.stdin.readline().split()))
start = 0
end = max(tree)
res = 0

while start <= end: # 시작점과 끝점이 교차하기전 동안
    total = 0
    mid = (start + end) //2 # 중간값 설정
    
    for t in tree: # tree list에서
        if t > mid: # 나무가 중간 값보다 크면
            total += (t-mid) # 나무를 자르고 남은 나무 길이를 계속 더함
        if total >= m: # 이미 필요한 길이가 넘으면
            break # 반복 그만
    
    if total < m: # 남은 길이들이 만족한 길이보다 짧으면
        end = mid-1 # 끝점을 앞으로 땡겨 더 크게 자르기로
    else:  # 남은 길이들이 만족한 길이보다 짧으면
        res = mid # 자르는 위치를 저장
        start = mid + 1 # 시작점을 뒤로 미뤄 더 작게 자르기로

print(res)

# Good explanation
from sys import stdin

N, M = map(int, stdin.readline().rstrip().split(' '))

input_ = stdin.readline().rstrip().split(' ')

trees = [0] * N

for i in range(N):
    trees[i] = int(input_[i])

def check(height): # 함수 사용
    result = 0
    for i in range(N):
        if trees[i] > height:
            result += trees[i] - height
    
    return result

front = 1 # 이분탐색 시작점
end = 1000000000 # 이분탐색 끝점

while front <= end: 
    mid = int((front + end) / 2)
    
    get = check(mid) # 함수로 자르고 남은 나무들의 합을 구함

    if get < M: # 남은 나무들의 길이 합이 원하는 값보다 작으면
        end = mid - 1 # 끝점을 옮겨 더 자르기
    
    else: # 남은 나무들의 길이 합이 원하는 값보다 크면
        front = mid + 1 # 시작점을 옮겨 덜 자르기
# 위 while문에서 도출된 mid 값으로 남은 나무들의 합 구하기
if check(mid) >= M: # 요구된 길이보다 크거나 같으면
    result = mid # 결과값 도출

else: # 요구된 길이보다 짧으면
    result = mid - 1 # 현재 mid보다 줄일 수 있는 최소의 길이로 줄임(-1)

print(result)