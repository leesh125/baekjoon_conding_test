# My turn
import sys
n = int(sys.stdin.readline())
words = set() # 중복 단어 제거를 위해

for _ in range(n):
    words.add(sys.stdin.readline().rstrip()) 

words = list(words) # list로 변환후
words.sort(key=lambda x:(len(x),x)) # 1. 길이 우선 정렬, 2. 사전 순 정렬

for word in words:
    print(word) # 출력

# Good explanation
import sys
word=set() # 중복 단어 제거 위해
for i in range(int(input())):
    word.add(sys.stdin.readline().rstrip())
word=list(word) # 리스트로 변환
word.sort() # 2. 사전 순 정렬 먼저
word.sort(key=lambda x:len(x)) # 1. 길이 우선 정렬
print("\n".join(word)) # 개행으로 word list를 join함 : 원소가 한 줄씩 출력