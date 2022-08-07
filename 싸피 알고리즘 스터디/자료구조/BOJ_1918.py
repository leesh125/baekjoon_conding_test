import sys
input = sys.stdin.readline

exp = input().rstrip()
ans = []
exp_stack = []
exp_dict = {'(':0,'+':1, '-':1, '*':2, '/':2} # 우선순위를 비교하기 위한 dict

for e in exp: # 하나씩 비교
    if 'A' <= e <= 'Z': # 숫자면 
        ans.append(e) # 그대로 답 문자열에 추가
    elif e == '(': # 소괄호 시작이면 
        exp_stack.append(e) # 기호 스택에 추가
    elif e == ')': # 소괄호 끝이면
        top = exp_stack.pop() # 가장 마지막에 있는 기호 빼내기
        while top != '(': # 그게 소괄호가 아니면
            ans.append(top) # 그 기호 답 문자열에 추가(이미 아래 조건문에 의해 소괄호 안에서 우선순위대로 출력되어있음)
            top = exp_stack.pop() # 빼내기
    else: # 연산기호이면
        # 기호 스택이 차있고 이미 스택에 있는 연산에 우선순위가 현재 연산기호보다 크면(선계산 해야함)
        while len(exp_stack) != 0 and exp_dict[exp_stack[-1]] >= exp_dict[e]:
            ans.append(exp_stack.pop()) # 답 문자열에 스택에 최상단에 있는 기호 추가
        exp_stack.append(e) # 현재 연산기호 연산스택에 추가

len_exp_stack = len(exp_stack)
for _ in range(len_exp_stack): # 남은 연산 기호 답 문자열에 넣어주기
    ans.append(exp_stack.pop()) # 스택 최상단에 있는 기호 우선순위가 뒤에 나오는 것보다 계속 작으면 그대로 남아있기 때문에

print(''.join(ans))