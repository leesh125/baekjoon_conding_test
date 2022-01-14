import sys
n = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))
nums_dic = {} # 배열안에 숫자중 하나가 다른 원소들보다 크면 작은 값들의 count수를 추가할 dict
nums_set = list(set(nums)) # 중복된 숫자는 체크를 하지 않아서 따로 생성함
nums_set.sort() # 정렬하여 count 수 순차 증가시키기
i=0
for ns in nums_set:
    nums_dic[ns] = i # dict에 count수 저장(가장 낮은값은 0: 그 다음 낮은값 1,,,)
    i+=1
for num in nums:
    print(nums_dic[num], end=' ') # dict의 value를 이용해 출력


import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().split()))
box = list(set(arr))
box = sorted(box)
key = {}
a = -1
for i in box:
    a += 1
    key[i] = a
for i in range(n):
    arr[i] = key[arr[i]] # 여기부터 다름 - 원래 배열에 dict 값을 주고
print(' '.join(map(str,arr)))  # 원래 배열을 str으로 map 한 다음 ' '.join으로 한 줄에 출력하게끔