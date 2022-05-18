# My turn
import sys
input = sys.stdin.readline

gears = []
cur_left,cur_right,score = 0,0,0

def clockwise(gear_list): # 시계방향 회전
    return gear_list[-1:-2:-1] + gear_list[0:-1]

def counter_clockwise(gear_list): # 반시계방향 회전
    return gear_list[1:] + gear_list[0:1]

def rotate(dir,gear_list): # 방향에 따라 다른 회전을 시켜주는 함수
    if dir == -1: # 반시계
        return counter_clockwise(gear_list)
    else: # 시계
        return clockwise(gear_list)

for i in range(4):
    gears.append(list(input().rstrip())) # 12시 방향 부터 시계방향으로(3번째, 7번째 것이 맞물려있는것)
for i in range(int(input())):
    gear, dir = map(int, input().split()) # 몇 번쨰 기어인지, 회전방향
    gear -= 1 # 1-인덱스 구조
    cur_dir = dir # 현재 회전 방향 담기(임시)
    cur_right, cur_left = gears[gear][2], gears[gear][6] # 현재 기어의 왼쪽 오른쪽 담기
    
    for left_gear in range(gear-1,-1,-1): # 왼쪽
        if gears[left_gear][2] != cur_left: # 현재 톱니의 왼쪽 톱니와 맞물려 있는 것이 다를 때
            cur_dir = (cur_dir * -1) # 현재 방향과 다르게 해서 회전 시킬거
            cur_left = gears[left_gear][6] # 현재 맞물린 왼쪽 톱니를 왼쪽기어의 왼쪽 톱니로 변환
            gears[left_gear] = rotate(cur_dir,gears[left_gear]) # 회전 시킨다
        else: # 아니면
            break # 더이상 회전 x
    
    cur_dir = dir # 현재 방향을 ㅗ초기화
    for right_gear in range(gear+1,4): # 오른쪽
        if gears[right_gear][6] != cur_right:
            cur_dir = (cur_dir * -1) 
            cur_right = gears[right_gear][2]
            gears[right_gear] = rotate(cur_dir,gears[right_gear])
        else:
            break
    gears[gear] = rotate(dir,gears[gear])

    
for i in range(4):
    if gears[i][0] == '1': # 12시 방향 톱니가 '1'이면
        score += int(2 ** i) #1,2,4,8로 더해주기
print(score)

# Good explanation
import sys
read = sys.stdin.readline
gears = []
for _ in range(4):
    gears.append(read().strip()) # 기어 추가

def rotate(target, num, spin, left = True, right= True): # 현재 기어, 현재 기어 번호, 회전 방향
    left_target, right_target = False, False # left,right 기어 false 기본값
    if (left): # 만약 left가 참이라면
        if num > 0 and num <= 3: # 현재기어 번호가 범위 내에 있으면
            left_target = gears[num-1] # 왼쪽기어를 왼쪽 타겟으로 설정
        else: left = False # 아니면 left를 false로
    if (right): # 만약 left가 참이라면
        if num >= 0 and num < 3:# 현재기어 번호가 범위 내에 있으면
            right_target = gears[num+1] # 오른쪽기어를 오른쪽 타겟으로 설정
        else:
            right = False # 아니면 right를 false로

    if left_target and left_target[2] != target[6]: # lefttarget(왼쪽 기어)가 있고 맞물려 있는게 다르다면
        rotate(left_target, num-1, -spin, left= True, right= False) # 재귀 (기어번호 -1,방향 바꾸고,right=false로)
    if right_target and right_target[6] != target[2]:
        rotate(right_target, num+1, -spin, left= False, right= True)

    if spin == 1: # 시계방향이면
        gears[num] = target[-1] + target[0:-1] # 회전
    else: # 반시계
        gears[num] = target[1::] + target[0] # 회전

for i in range(int(read())):
    num, spin = map(int, read().split()) # 현재 기어 번호, 방향 추출
    rotate(gears[num-1],num-1, spin) # 회전시키기
ans = ''
for i in range(3,-1,-1):
    ans += gears[i][0]

print(int(ans,2)) # 문자열로 받아서 2진수 변환