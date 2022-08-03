import sys
input = sys.stdin.readline

string = input()[:-1]
bomb = input()[:-1]
stack = []
idx = 0
len_string = len(string)
len_bomb = len(bomb)

stack.append(string[0])

for i in range(1,len_string):
    if stack[-1] == bomb[idx]:
        if idx == len_bomb-1:
            for _ in range(len_bomb):
                stack.pop()
            continue
        else:
            idx += 1
            stack.append(string[i])
            
    else:
        idx = 0
        stack.append(string[i])
    print(stack, idx)
# print(stack)