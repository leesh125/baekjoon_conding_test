# from itertools import combinations

# n,m = map(int, input().split())
# nums = input().split()
# nums.sort(key=lambda x:int(x))
# ans = [0] * m
# visited = set()

# for p in combinations(nums, m):
#     s = ' '.join(p)
#     if s not in visited:
#         visited.add(s)
#         print(s)



def permutation(idx,cnt):
    if cnt == m:
        str_ans = ''.join(map(str,ans))
        if str_ans not in dic:
            dic[str_ans] = True
            print(*ans)
        return
    
    for i in range(idx,n):
        if not visited[i]:
            visited[i] = True
            ans[cnt] = nums[i]
            permutation(i+1,cnt+1)
            visited[i] = False

n,m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
ans = [0] * m
visited = [False] * n
dic = {}

permutation(0,0)