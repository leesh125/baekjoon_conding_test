# My turn
import sys
from itertools import permutations
input = sys.stdin.readline
INF = int(1e10) # 임의의 무한대 수
N = int(input())
numbers = list(map(int,input().split())) # 숫자 조합
ops = list(map(int,input().split())) # 연산자 갯수
operators = [] # 연산자들의 모임
max_num, min_num = -INF, INF # 최댓값, 최솟값 초기 설정

for i in range(4): # 연산자 모임을 한 리스트에 몰아넣기
    if i == 0:
        for j in range(ops[i]):
            operators.append('+')
    elif i == 1:
        for j in range(ops[i]):
            operators.append('-')
    elif i == 2:
        for j in range(ops[i]):
            operators.append('*')
    elif i == 3:
        for j in range(ops[i]):
            operators.append('//')
all_combi = set(permutations(operators, N-1))

# 수식을 계산하는 함수
def get_max_min(combi): 
    exp,stack = [],[] # 수식, 스택
    for num, operator in zip(numbers,combi): # 숫자, 연산자 번갈아 넣기
        exp.append(num) # 숫자
        exp.append(operator) # 연산자
    exp.append(numbers[-1]) # 남은 숫자 추가
    
    for i in range(len(exp)):
        stack.append(exp[i]) # 수식 하나씩 삽입
        
        if len(stack) == 3: # 피연산자 , 연산자, 피연산자가 수식일 경우 연산 진행
            if stack[1] == '+':
                stack[0] = stack[0] + stack[2]
                stack.pop()
                stack.pop()
            elif stack[1] == '-':
                stack[0] = stack[0] - stack[2]
                stack.pop()
                stack.pop()
            elif stack[1] == '*':
                stack[0] = stack[0] * stack[2]
                stack.pop()
                stack.pop()
            elif stack[1] == '//':
                if stack[0] < 0 and stack[2] > 0: # 음수를 나눌 때 따로 계산
                    stack[0] *= -1
                    stack[0] = stack[0] // stack[2] * -1
                else:
                    stack[0] = stack[0] // stack[2]
                stack.pop()
                stack.pop()
    return stack[0] # 완성된 수식 반환

for combi in all_combi: # 모든 수식 순회
    res = get_max_min(combi) # 결과값 도출
    max_num = max(max_num, res) # 최댓값 갱신
    min_num = min(min_num, res) # 최솟값 갱신
print(max_num)
print(min_num)

# Good Explanation
import sys
input = sys.stdin.readline

N = int( input() )
nums = list( map( int, input().split() ) ) # 숫자들
oper = list( map( int, input().split() ) ) # 각 연산자의 갯수

# method 2
def backtrack( prevVal, size, idx, plus, minus, multi, divide ): # 누적 수식 값, 깊이, 인덱스, 연산자들
	global max, min
	if size == N - 1: # 깊이가 끝까지 도달했다면
		if max < prevVal: # 최댓값 갱신
			max = prevVal
		if min > prevVal: # 최솟값 갱신
			min = prevVal
	else: # 백트래킹
		if plus: # '+' 연산자의 갯수가 1 이상이면
            # 다음 숫자 + 한 후 재귀
			backtrack( prevVal + nums[idx], size + 1, idx + 1, plus - 1, minus, multi, divide )

		if minus:
			backtrack( prevVal - nums[idx], size + 1, idx + 1, plus, minus - 1, multi, divide )

		if multi:
			backtrack( prevVal * nums[idx], size + 1, idx + 1, plus, minus, multi - 1, divide )

		if divide:
			if prevVal < 0:
				backtrack( -(abs(prevVal) // nums[idx]), size + 1, idx + 1, plus, minus, multi, divide - 1 )
			else:
				backtrack( prevVal // nums[idx], size + 1, idx + 1, plus, minus, multi, divide - 1 )
max = -(10**9+1)
min = 10 ** 9 + 1
backtrack( nums[0], 0, 1, *oper ) # backtracking 함수 실행
print( max, min, sep = '\n' )