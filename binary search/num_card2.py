# My turn
import sys
from bisect import bisect_left, bisect_right

n = int(sys.stdin.readline())
arr1 = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))
arr1.sort()

# bisect를 이용한 함수
def count_by_range(a, left, right): 
    # bisect_right(a, right) : 정렬된 배열에서 순서를 유지하면서 right를 삽입할 가장 오른쪽 인덱스를 반환
    right = bisect_right(a, right) 
    # bisect_right(a, right) : 정렬된 배열에서 순서를 유지하면서 right를 삽입할 가장 왼쪽 인덱스를 반환
    left = bisect_left(a, left)
    return right - left # 결국 해당 인덱스가 얼마나 포함되어 있는지 반환

for a in arr2:
    print(count_by_range(arr1,a,a), end=' ')


# Good explanation
from sys import stdin
_ = int(input())
n = [int(i) for i in stdin.readline().split()]
_ = int(input())
m = [int(i) for i in stdin.readline().split()]

hashmap = {} # dictionary를 사용
for i in n:
    if i in hashmap: # 처음 배열에 key가 있다면 해당 key의 value +1
        hashmap[i] += 1
    else: # 처음 배열에 key가 없다면 1로 지정
        hashmap[i] = 1

print(' '.join(str(hashmap[i]) if i in hashmap else '0' for i in m)) # 해쉬맵에서 key의 value 꺼내기(없으면 0 출력)
