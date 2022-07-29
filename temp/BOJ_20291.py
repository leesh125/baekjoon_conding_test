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
