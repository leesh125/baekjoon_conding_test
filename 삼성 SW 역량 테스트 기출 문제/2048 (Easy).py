# My turn
import sys, copy
from itertools import product

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]  # 받은 격자
check = [[0 for _ in range(N)] for _ in range(N)]  # 이동했는지 체크하는 격자
dir = [0, 1, 2, 3]  # 위,오른쪽,아래,왼쪽
all_combi = list(product(dir, repeat=5))  # 모든 경우의 수 구하기(ex. 위위위위위, 위위위위오 ... 왼왼왼왼왼)
max_num = 0  # 최고 점수 담을 변수

# 위로 이동하는 함수
def move_up(graph, check):
    for i in range(N):  # 열 기준으로
        while True:  # 반복
            move = 0  # 순회하면서 바꾸는게 있으면 세기 위한 cnt
            for j in range(N - 1):  # 첫째행부터 마지막 전 행까지
                if graph[j][i] == 0 and graph[j + 1][i] != 0:  # 지금 행 값이 0이고 다음 행 값이 숫자면
                    # 0값과 숫자 바꾸기
                    graph[j][i], graph[j + 1][i] = graph[j + 1][i], graph[j][i]
                    move += 1  # 이동했으니 += 1
                elif (  # 0이 아니고 같은 숫자이고 해당 행과 다음 행이 바뀌지 않은 값이라면
                    graph[j][i] != 0
                    and graph[j + 1][i] == graph[j][i]
                    and check[j][i] == 0
                    and check[j + 1][i] == 0  # 한 칸씩 빠지기 때문에 다음 행값도 고려
                ):
                    # 합친 값을 넣고 나머지는 0값 넣기
                    graph[j][i], graph[j + 1][i] = graph[j + 1][i] + graph[j][i], 0
                    check[j][i] = 1  # 현재 행만 check 하기(다음 행은 바뀔 수 있음 언제든)
                    move += 1  # 이동했으니 += 1
            if move == 0:  # 이동이 이제는 없으면
                break  # 빠져나오기
    return graph  # 변환된 그래프 반환


# 오른쪽 이동
def move_right(graph, check):
    for i in range(N):
        while True:
            move = 0
            for j in range(N - 2, -1, -1):
                if graph[i][j] != 0 and graph[i][j + 1] == 0:
                    graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
                    move += 1
                elif (
                    graph[i][j] != 0
                    and graph[i][j] == graph[i][j + 1]
                    and check[i][j + 1] == 0
                    and check[i][j] == 0
                ):
                    graph[i][j], graph[i][j + 1] = 0, graph[i][j] + graph[i][j + 1]
                    check[i][j + 1] = 1
                    move += 1
            if move == 0:
                break
    return graph


# 아래로 이동
def move_down(graph, check):
    for i in range(N):
        while True:
            move = 0
            for j in range(N - 2, -1, -1):
                if graph[j][i] != 0 and graph[j + 1][i] == 0:
                    graph[j][i], graph[j + 1][i] = graph[j + 1][i], graph[j][i]
                    move += 1
                elif (
                    graph[j][i] != 0
                    and graph[j + 1][i] == graph[j][i]
                    and check[j + 1][i] == 0
                    and check[j][i] == 0
                ):
                    graph[j][i], graph[j + 1][i] = 0, graph[j + 1][i] + graph[j][i]
                    check[j + 1][i] = 1
                    move += 1
            if move == 0:
                break
    return graph


# 왼쪽 이동
def move_left(graph, check):
    for i in range(N):
        while True:
            move = 0
            for j in range(N - 1):
                if graph[i][j] == 0 and graph[i][j + 1] != 0:
                    graph[i][j], graph[i][j + 1] = graph[i][j + 1], graph[i][j]
                    move += 1
                elif (
                    graph[i][j] != 0
                    and graph[i][j] == graph[i][j + 1]
                    and check[i][j] == 0
                    and check[i][j + 1] == 0
                ):
                    graph[i][j], graph[i][j + 1] = graph[i][j] + graph[i][j + 1], 0
                    check[i][j] = 1
                    move += 1
            if move == 0:
                break
    return graph


# 그래프에서 최댓값 구하기
def get_max(copy_graph):
    max_num = 0
    for g in copy_graph:
        max_num = max(max_num, max(g))
    return max_num


# bfs 탐색(?) 깡구현에 가까운듯
def bfs(combi):
    copy_graph = copy.deepcopy(graph)  # 2차원 배열 깊은 복사로 원본 값 건들이지 않기
    for c in combi:  # 조합을 하나씩 비교
        tmp_check = copy.deepcopy(check)  # check 리스트 깊은 복사
        if c == 0:  # 위로 가는거
            copy_graph = move_up(copy_graph, tmp_check)
        elif c == 1:  # 오른쪽으로 가는거
            copy_graph = move_right(copy_graph, tmp_check)
        elif c == 2:  # 아래로 가는거
            copy_graph = move_down(copy_graph, tmp_check)
        elif c == 3:  # 왼쪽으로 가는거
            copy_graph = move_left(copy_graph, tmp_check)
    return get_max(copy_graph)  # 최댓값 구하기


for combi in all_combi:  # 모든 조합 순회
    max_num = max(max_num, bfs(combi))  # 최댓값 갱신

print(max_num)

# Good Explanation
N = int(input())
original_board = [list(map(int, input().split())) for _ in range(N)]

direction = ["l", "u", "r", "d"]  # 방향

# 2차원 배열에서 최댓값 구하기
def max_element(matrix):
    result = 0
    for rows in matrix:
        rows.append(result)
        result = max(rows)
    return result


# 왼쪽 이동
def move_left(mat):
    result = []
    for rows in mat:  # 행
        new_row = []  # 새로운 행
        temp = 0  # 0이 아닌 값 담을 변수
        for num in rows:  # 열
            if num == 0:  # 0 이면 지나가기
                continue
            if temp == num:  # temp와 num이 같다면
                new_row[-1] *= 2  # 마지막에 추가된 값을 *=2로
                temp = 0  # 임시변수 0(한 이동에 한번만 합쳐짐)
            else:  # temp와 num이 다르면
                new_row.append(num)  # 새 행에 해당 숫자 추가
                temp = num  # temp에 숫자 추가
        new_row += [0] * (len(rows) - len(new_row))  # 새 행에 원래 행의 길이까지만큼 0을 추가한다
        result.append(new_row)  # 새로운 2차원 배열을 만들기

    return result


def move_up(mat):  # 위로 이동
    result = move_left(list(map(list, zip(*mat))))  # 행과 열을 교환 후, 왼쪽 이동 함수
    return list(map(list, zip(*result)))  # 다시 행과 열을 교환


def move_right(mat):
    result = []
    for rows in mat:  # 행
        rows.reverse()  # 행을 뒤집음(역순)
        new_row = []  # 새로운 행
        temp = 0  # 0이 아닌 값 담을 변수
        for num in rows:  # 열
            if num == 0:
                continue
            if temp == num:
                new_row[-1] *= 2
                temp = 0
            else:
                new_row.append(num)
                temp = num
        new_row += [0] * (len(rows) - len(new_row))
        new_row.reverse()  # 역순을 원래대로 돌림
        result.append(new_row)  # 새로운 리스트에 담음
    return result


def move_down(mat):  # 아래로 이동
    result = move_right(list(map(list, zip(*mat))))  # 행과 열을 교환 후, 오른쪽 이동 함수
    return list(map(list, zip(*result)))  # 다시 행과 열을 교환


# dfs 탐색
def dfs(board, n):
    global answer
    if n == 5:  # 5번 탐색이 완료되면
        answer = max(answer, max_element(board))  # 최댓값 찾기 and 갱신
        return

    else:  # 탐색 중이면 위, 오른쪽, 아래, 왼쪽 dfs 탐색
        dfs(move_left(board), n + 1)
        dfs(move_right(board), n + 1)
        dfs(move_up(board), n + 1)
        dfs(move_down(board), n + 1)


answer = 0
dfs(original_board, 0)
print(answer)
