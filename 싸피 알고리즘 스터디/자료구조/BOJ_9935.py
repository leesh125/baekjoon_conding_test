import sys
input = sys.stdin.readline

string = input()[:-1] # 문자열
bomb = input()[:-1] # 폭탄 문자열
len_bomb = len(bomb) #폭탄 길이
stack = [] # 스택

for s in string: # 문자 하나씩
    stack.append(s) # 스택에 추가
    # 현재 문자가 폭탄 문자열에 마지막 문자와 같고 이전값과 비교했을때 폭탄 문자열이라면
    if s == bomb[-1] and bomb == ''.join(stack[-len_bomb:]):
        for _ in range(len_bomb):
            stack.pop() # 폭탄 문자열 만큼 빼내기

print(''.join(stack) if stack else 'FRULA') # 출력

# Good Explanation
origin, to_remove,*a = open(0, 'rb').read().split(b'\n')
L = len(to_remove)

s = bytearray()
for c in origin:
    s.append(c)
    if to_remove[-1] == c:
        if to_remove == s[-L:]:
            del s[-L:]
print(s.decode() if s else 'FRULA')