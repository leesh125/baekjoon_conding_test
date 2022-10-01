# from itertools import combinations_with_replacement

# n,m = map(int, input().split())
# nums = input().split()
# nums.sort(key=lambda x:int(x))
# ans = [0] * m
# visited = set()

# for p in combinations_with_replacement(nums, m):
#     s = ' '.join(p)
#     if s not in visited:
#         visited.add(s)
#         print(s)



def dup_combination(idx,cnt):
    if cnt == m:
        str_ans = ' '.join(map(str,ans))
        if str_ans not in dic:
            dic[str_ans] = True
            print(*ans)
        return
    
    for i in range(idx,n):
        ans[cnt] = nums[i]
        dup_combination(i,cnt+1)
        

n,m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = [0] * m
visited = [False] * n
dic = {}

dup_combination(0,0)