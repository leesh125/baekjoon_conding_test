import sys
input = sys.stdin.readline

dic = dict() # 알파벳에 따른 값 담을 dictionary
stack = [] # 후위 표기식 담을 stack
N = int(input()) 
exp = input().rstrip()

for i in range(65, 65+N):
    dic[chr(i)] = int(input()) # 알파벳에 따른 숫자 담기

for e in exp:
    if 'A' <= e <= 'Z': # or  if e.isupper() => 문자열(e)이 대문자로 이루어져 있는지
        stack.append(dic[e]) # 추가
    else: # 연산자이면
        suf = stack.pop() # 빼내기
        pre = stack.pop()
        
        if e == '+': stack.append(pre + suf) # 값에 맞게 연산
        elif e == '-': stack.append(pre - suf)
        elif e == '*': stack.append(pre * suf)
        elif e == '/': stack.append(1.0 * pre / suf)
    
print("%.2f" %stack[0])

        
