import sys
input = sys.stdin.readline

N,C = map(int,input().split())
nums = list(map(int,input().split()))
dic = {}
n_dic = {}

for n in nums:
    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1
for d in dic:
    if dic[d] not in n_dic:
        n_dic[dic[d]] = [d]
    else:
        n_dic[dic[d]].append(d)
    
for key in sorted(n_dic.keys(),reverse=True):
    for n in n_dic[key]:
        for i in range(key):
            print(n, end=' ')