# My Turn
import sys

input = sys.stdin.readline

exam_room = int(input())  # 총 시험장 수
total_student = list(map(int, input().split()))  # 시험장 당 학생수
main_s, sub_s = list(map(int, input().split()))  # 감독관, 부감독관의 역량

cnt = exam_room  # 차피 1 강의실엔 1명의 총 감독관이 있어야 함
left_student = []  # 남은 학생 수
for i in range(exam_room):  # 시험장 수 만큼
    left_student.append(total_student[i] - main_s)  # 남은 감독해야하는 학생들 담기

for left in left_student:  # 남은 감독해야하는 학생들
    if left > 0:  # 0 이상이라면
        # 나머지가 딱 맞으면 그대로 부감독관 배정, 나머지가 있다면 +1
        cnt += left // sub_s if left % sub_s == 0 else left // sub_s + 1
print(cnt)

# Good Explanation
input()
A = list(map(int, input().split()))  # 시험장 당 학생 수
B, C = map(int, input().split())  # 감독관, 부감독관 역량
dic = [0] + [1] * B + [0] * (1000000 - B)  # 감독관 숫자만큼은 1로 설정(시험장 당 들어가는 학생 수를 dict로)
ans = 0

for a in A:  # 시험장 당 학생 수 순회

    if not dic[a]:  # 초기: 총 감독관의 역량보다 많은 학생 수가 있다면, 나중: 같은 학생 수는 이미 처리된 부감독 배치로 반환
        i, j = divmod(a - B, C)  # 감독관의 역량을 제외한 학생수와 부감독관의 역량을 나눈다(몫, 나머지로 분할)
        dic[a] = i + 2 if j else i + 1  # 나머지가 0이 아니면 몫 + 2(총 감독관까지 포함해서), 나머지 0이면 몫 + 1

    ans += dic[a]  # 누적

print(ans)
