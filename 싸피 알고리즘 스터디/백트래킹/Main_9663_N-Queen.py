def possible(row):
    for i in range(1,row): # 1행부터 현재행까지
        # 같은 열의 놓여있거나, 대각선으로 같이 있을때 
        if chess[i] == chess[row] or row-i == abs(chess[row] - chess[i]):
            return False # 안됨
    return True

def nQueen(row):
    global ans
    if row > N: # 끝까지 아무 탈 없이 도달하면
        ans+=1 # 경우의 수 1 증가
        return

    for i in range(1,N+1): # 현재 행의 넣을 숫자
        chess[row] = i # 현재 행의 현재 숫자(열) 넣기
        if possible(row): # 지금 행까지를 가능한지 비교
            nQueen(row+1) # 다음행으로 넘어감

N = int(input())
chess = [0] * (N+1) # 1행 1열 기준 시작
ans = 0
nQueen(1) # 1행부터 시작
print(ans)