from sys import stdin

K, N = map(int,stdin.readline().rstrip().split())
lines = [int(stdin.readline().rstrip()) for _ in range(K)]
start = 0
end = 2 ** 31 # 끝 점 기준
ans = []

# lan선 자르는 함수
def cut(mid):
    total = 0

    for i in range(K):
        total += (lines[i] // mid) # 한 줄 당 지정한 길이로 자를경우 줄들의 합
        if total >= N: # 요구한 것 보다 높으면 바로 빠져나오기
            break

    return total

while start <= end:
    mid = (start + end) // 2
    
    res = cut(mid) # 중간 크기로 자르기

    if res < N: # 주어진 길이로 잘랐을 때, 나온 줄들의 합이 요구보다 적으면
        end = mid - 1 # 더 짧게 자르기
    else: # 주어진 길이로 잘랐을 때, 나온 줄들의 합이 요구보다 크면
        # ans.append(mid) # 그 기준을 ans에 담기
        start = mid + 1 # 더 길게 자르기
        ans = mid # 기준점

# print(max(ans)) # 기준들 중 최고값 출력
print(ans)


# Good explanation
from sys import stdin
K, N = map(int,stdin.readline().split())
li = list(map(int,stdin.readlines()))
h, l = sum(li)//N, 1 # 끝 점 기준을 (줄들의 합/요구된 줄 수)으로 지정 (이유: 이 길이보다 길어봤자 요구되는 줄 수를 만족못함)
while l <= h :
    mid = (h+l)//2 # 중간점 잡기
    cnt = sum([x//mid for x in li]) # 줄들을 자르기, 줄들의 수 합
    if cnt < N: # 주어진 길이로 잘랐을 때, 나온 줄들의 합이 요구보다 적으면
        h = mid - 1 # 더 짧게 자르기
    elif cnt >= N: # 주어진 길이로 잘랐을 때, 나온 줄들의 합이 요구보다 크면
        l = mid + 1 # 더 길게 자르기
        ans = mid # 기준점
print(ans)