import sys
input = sys.stdin.readline

def isGoodWord(word):
    stk = []
    if len(word) % 2 == 1: return False
    for w in word:
        if not stk:
            stk.append(w)
        else:
            if stk[-1] == w:
                stk.pop()
            else:
                stk.append(w)
    if stk: return False
    else: return True

cnt = 0
for _ in range(int(input())):
    word = input().rstrip()
    if isGoodWord(word): cnt += 1
print(cnt)