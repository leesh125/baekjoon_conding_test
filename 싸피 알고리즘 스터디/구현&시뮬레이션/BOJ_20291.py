import sys,re
input = sys.stdin.readline

# dic = {}
# for _ in range(int(input())):
#     ex_str = re.split(r'[.]',input().rstrip())[1]
#     dic[ex_str] = 1 if ex_str not in dic else dic[ex_str] + 1
# for d in sorted(dic):
#     print(d, dic[d])

dic = {}
for _ in range(int(input())):
    str = input().rstrip().split('.')[1]
    dic[str] = 1 if str not in dic else dic[str] + 1
for d in sorted(dic):
    print(d,dic[d])

# Good Explanation
import sys
input = sys.stdin.readline
def sol():
    d=dict() # dictionary
    n=int(input()) 
    for line in range(n): # 읽어 들인 만큼
        name,ext=input().strip().split('.') # split한 것 중 name 버리고 확장자명만 뽑음
        d[ext]=d.get(ext,0)+1 # 없으면 새로 1, 있으면 기존값 +1
    print('\n'.join(a+' '+str(d[a]) for a in sorted(d.keys()))) # 정렬된 것 조인해서 한줄 출력
sol()