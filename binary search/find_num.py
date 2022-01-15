import sys
n = int(sys.stdin.readline())
arr1 = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
arr2 = list(map(int,sys.stdin.readline().split()))
arr1.sort()

# while문 방법
# def binary_search(arr,target,start,end):
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == target:
#             return 1
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             start = mid + 1
#     return 0

# 재귀함수 방법
def binary_search(arr,target,start,end):
    if start > end: # 시작 인덱스가 끝 인덱스보다 커지면(값을 못 찾으면 st,ed가 같은곳을 바로보고 start가 +1이 됨)
        return 0
    mid = (start + end) //2 # 중간 인덱스 지점
    if arr[mid] == target: # 찾는 값이면 return 1
        return 1
    elif arr[mid] > target: # 찾는 값보다 중간 값이 크면 
        return binary_search(arr1,target,start,mid-1) # 끝 지점을 mid -1
    else: # 찾는 값보다 중간 값이 작으명
        return binary_search(arr1,target,mid+1,end) # 시작 지점을 mid + 1
        
for a2 in arr2: # target 배열 원소 하나씩
    print(binary_search(arr1,a2,0,n-1)) # arr1 배열 탐색하기
