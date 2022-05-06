# import sys
# member = [list(sys.stdin.readline().split()) for _ in range(int(input()))]
# member.sort(key=lambda x: int(x[0])) # 첫번째 원소(나이) 기준으로 정렬
# for age, name in member: # 배열 출력
#     print(age,name) 

# # Good explanation 1
# import sys

# lst = sys.stdin.readlines()[1:] # 첫 번째 입력 버리고 끝까지 리스트에 담기
# lst.sort(key=lambda x: int(x.split()[0])) # 첫번째 원소(나이) 기준으로 정렬
# print(''.join(lst)) # 개행 문자가 포함이기에 자동 줄 바꿈이 됨


# Good explanation 2
from sys import stdin, stdout

users_by_age = [[] for _ in range(200+1)] # 나이는 최대 200살

for line in stdin.read().splitlines(True)[1:]: # 한 줄 살펴보기(ex, 21 Junkyu)
    users_by_age[int(line.split()[0])].append(line) # 나이를 인덱스로 배열에 저장

# sys.stdout.write = 개행 제거
stdout.write(''.join(
    ''.join(u) 
    for u in
    users_by_age # 나이를 인덱스로 회원을 가지고 있는 배열(같은 나이는 순서대로기에 통과)
))