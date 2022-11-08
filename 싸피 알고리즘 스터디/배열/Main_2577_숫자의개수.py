import sys
input = sys.stdin.readline

ans = 1
dic = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for _ in range(3): ans *= int(input())
for s in str(ans): dic[s] += 1
for value in dic.values():
    print(value)