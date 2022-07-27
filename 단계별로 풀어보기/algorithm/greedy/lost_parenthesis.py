# My turn
s = input()
math_exp = s.split('-')   # 입력 받은 수 '-'로 나누기, -로 끊겨지기 때문에 첫번째에서 나머지 뒤 원소들을 빼주면 된다

for i in range(len(math_exp)):
    if math_exp[i][0] == '0':    # 앞에 0이 입력될 경우
        math_exp[i] = math_exp[i].lstrip('0')  # 0 제거

    if '+' in math_exp[i]:
        arr = list(map(int,math_exp[i].split('+')))  # '+'가 있는 원소는 
        math_exp[i] = sum(arr)  # 다 더한 값을 원소로
    else:
        math_exp[i] = int(math_exp[i])

val = math_exp[0]

for i in range(1,len(math_exp)):  # 첫째 원소에서 나머지 원소들 빼기
    val -= math_exp[i]

print(val)


# Good explanation

# 1. 들어온 수를 -로 나누고
# 2. 나눈 것을 +로 다시 나누고(+가 없는 그냥 양수여도 상관없음)
# 3. map함수를 통해 int형으로 바꿔준 후([['10+20+3']] => 10,20,3)
# 4. sum을 통해 최종적으로 해당 원소의 수식(1번에서 나눈 수식)의 합을 구한다
e = [sum(map(int, x.split('+'))) for x in input().split('-')]
# 5. 첫번째 양수에서 나머지 뒤의 합 원소들을 빼준다
print(e[0]-sum(e[1:]))

