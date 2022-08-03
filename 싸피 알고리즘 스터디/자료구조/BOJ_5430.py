# import sys
# from collections import deque
# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     p = list(input().rstrip())
#     n = int(input())
#     r_cnt = 0
    
#     nums = deque(list(input().lstrip('[').rstrip().rstrip(']').split(',')))
#     if nums[0] == '': nums.pop()
#     for i in range(len(p)):
#         flag = True
#         if p[i] == 'R':
#             r_cnt += 1
#         else:
#             if len(nums) == 0:
#                 flag = False
#                 break
#             else:
#                 if r_cnt % 2 == 0:
#                     nums.popleft()
#                 else:
#                     nums.pop()

#     if r_cnt % 2 == 1:
#         nums.reverse()
#     if flag:
#         print('['+','.join(list(nums))+']')
#     else:
#         print('error')
        
    # print(nums)


# Good Explanation
from sys import stdin

input = stdin.readline


def solve():

    for _ in range(int(input())):
        # 'RR' 는 안뒤집는 것과 동일하므로 ''로 바꿔준다
        p = [*map(len, input()[:-1].replace('RR', '').split('R'))]

        n = int(input())
        arr = input()[1:-2].split(',')
        # [left, right) 가 출력된다
        left, right = sum(p[::2]), n - sum(p[1::2])

        if left <= right:
            # len(p) % 2 == 1 인 경우 왼쪽에서 오른쪽 방향
            arr = arr[left:right] if len(p) % 2 else reversed(arr[left:right])
            print(f"[{','.join(arr)}]")
        else:
            print('error')


if __name__ == '__main__':
    solve()