n, k = map(int, input().split()) # 숫자 2개 입력받기
arr = [int(input()) for _ in range(n)] # 동전 종류 입력받기
cnt = 0

for i in reversed(range(len(arr))): # 역순으로 동전을 탐색
    if k // arr[i] != 0:  # 해당 동전의 종류와 나눠떨어지면
        cnt += k // arr[i] # 그 몫만큼 count 증가
        k %= arr[i] # 초기 입력받은 금액을 나머지 금액으로 초기화
    else:
        continue

print(cnt)