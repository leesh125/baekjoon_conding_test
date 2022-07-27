import sys

n = int(sys.stdin.readline())
count = [0] * 8005 # 절대값으로 인해 넉넉하게 배열 설정
nums=[]

for i in range(n):
    nums.append(int(sys.stdin.readline()))
    count[4000+nums[i]] += 1

nums = sorted(nums)
max_num = max(count)
max_arr = []

for i in range(8002):
    if count[i] == max_num:
        max_arr.append(i)

print(round(sum(nums)/len(nums))) # 배열 평균값
print(nums[len(nums)//2]) # 배열 중간 값
if len(max_arr) == 1: # 최빈값이 하나일 경우
    print(max_arr[0]-4000) # 그 하나를 출력
else:
    print(max_arr[1]-4000) # 두번째로 작은값 출력
print(max(nums)-min(nums)) # 배열 범위