import sys

def binary_search(left, right):
    
    if left > right:
        return left

    mid = (left + right) // 2 # 임의의 mid 값 구하기
    cnt = 0

    for i in range(1,n+1):
        cnt += min(mid//i,n) # 배열안에서 mid 값보다 작은 수들의 갯수 구하기

    if cnt >= k: # 그 갯수가 k 보다 크거나 같으면(찾고자 하는 값 보다 mid값이 크거나 같음)
        return binary_search(left, mid-1) # 범위를 더 적게 좁히기
    else:
        return binary_search(mid+1, right) # 범위를 더 크게 좁히기
  
def binary_search2(left, right):
    ans = 0
    while left <= right:
        mid = (left + right) // 2 # 임의의 중간값

        cnt = 0
        
        for i in range(1,n+1):
            cnt += min(mid // i, n) # 중간값보다 작은 값들의 갯수
        
        if cnt >= k: # 그 갯수가 k 보다 크면(조건을 만족)
            ans = mid
            right = mid - 1
        else: # 작으면 
            left = mid + 1
    return ans



n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

# right를 k로 놓은 이유: 배열에 인덱스 k에 값은 항상 내가 찾고자 하는 값보다 작기 때문
# print(binary_search(1,k))
print(binary_search2(1, k)) 